
import { createRequire } from "module";
const require = createRequire(import.meta.url);


const express = require("express");

const { PythonShell } = require("python-shell");


const dotenv = require("dotenv");
const bodyParser = require("body-parser");
const cookieParser = require("cookie-parser");
import mongoose from 'mongoose';
dotenv.config();
const app = express();
app.set("view engine", "ejs");
app.use(bodyParser.urlencoded({extended: true}));
app.use(cookieParser());
app.use(express.static("public"));

import chatRouter from "./routes/chat-routes.js";
import journalRouter from "./routes/journal-routes.js";
import router from "./routes/user-routes.mjs";
app.use("/api/chatBot",chatRouter); 

app.use("/user",router);
app.use("/post",journalRouter);
app.use("/chatbox",chatRouter);
mongoose.connect(process.env.MongoDB_Connection_Link, {
    useNewUrlParser: true,
}).then(() => {
    console.log("Connected to the db");
}).catch((err) => {
    console.log(err + " not connected to db");
});

app.get("/", function(req,res,next){
    res.render('home_page');
})

app.get("/predict", function(req,res){
    res.render('predict', { result: null });
})

app.post("/predict", function(req,res){
    const body = req.body || {};

    const first = (v) => Array.isArray(v) ? v[0] : v;
    const num = (v) => {
      const n = Number(first(v));
      return Number.isFinite(n) ? n : 0;
    };
    const yn = (v) => {
      const x = first(v);
      return x === "1" || x === 1 || x === true || x === "yes" ? 1 : 0;
    };

    const parseBloodGroupCode = (v) => {
      const raw = String(first(v) ?? "").trim().toUpperCase();
      const asNum = Number(raw);
      if (Number.isFinite(asNum) && asNum !== 0) return asNum;

      const map = {
        "A+": 11,
        "A-": 12,
        "B+": 13,
        "B-": 14,
        "O+": 15,
        "O-": 16,
        "AB+": 17,
        "AB-": 18,
      };
      return map[raw] || 15;
    };

    const age = num(body.b);
    const pregnant = yn(body.c);
    const abortions = yn(body.d);
    const weightKg = num(body.s);
    const heightCm = num(body.t);
    const bmi = num(body.u);
    const bloodGroup = parseBloodGroupCode(body.v);
    const pulse = num(body.w);
    const cycleMonths = num(body.x);
    const cycleDays = num(body.y);
    const marriageYears = num(body.z);
    const hipIn = num(body.za);
    const waistIn = num(body.zb);

    const whr = hipIn > 0 ? (waistIn / hipIn) : 0;

    // Dataset uses Cycle(R/I) codes: {2,4,5}. Use a simple heuristic from the form.
    const cycleRI = cycleMonths > 1 ? 4 : 2;

    const payload = {
      " Age (yrs)": age,
      "Weight (Kg)": weightKg,
      "Height(Cm) ": heightCm,
      "BMI": bmi,
      "Blood Group": bloodGroup,
      "Pulse rate(bpm) ": pulse,
      "Cycle(R/I)": cycleRI,
      "Cycle length(days)": cycleDays,
      "Marraige Status (Yrs)": marriageYears,
      "Pregnant(Y/N)": pregnant,
      "No. of aborptions": abortions,
      "Hip(inch)": hipIn,
      "Waist(inch)": waistIn,
      "Waist:Hip Ratio": whr,
      "Weight gain(Y/N)": yn(body.l),
      "hair growth(Y/N)": yn(body.m),
      "Skin darkening (Y/N)": yn(body.n),
      "Hair loss(Y/N)": yn(body.o),
      "Pimples(Y/N)": yn(body.p),
      "Fast food (Y/N)": yn(body.q),
      "Reg.Exercise(Y/N)": yn(body.r),
    };

    const options = {
      mode: "text",
      pythonOptions: ["-u"],
      scriptPath: "ml",
      args: [JSON.stringify(payload)],
    };

    PythonShell.run("predict_pcos.py", options)
      .then((out) => {
        const raw = Array.isArray(out) ? out.join("\n") : String(out || "");
        let parsed;
        try {
          parsed = JSON.parse(raw);
        } catch (e) {
          return res.render("predict", { result: "Prediction service returned an unexpected response. Please try again." });
        }

        const probText = typeof parsed.probability === "number" ? ` (probability: ${(parsed.probability * 100).toFixed(1)}%)` : "";
        const result = `${parsed.message}${probText}`;
        return res.render("predict", { result });
      })
      .catch((err) => {
        console.log(err);
        return res.render("predict", { result: "Prediction service is unavailable. Please train the model and try again." });
      });
})
const PORT = process.env.PORT || 5000;
app.listen(PORT, function(){
    console.log(`server is running on ${PORT}.......`);
});

