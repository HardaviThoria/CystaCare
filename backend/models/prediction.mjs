import mongoose from "mongoose";

const predictionSchema = new mongoose.Schema(
  {
    user: { type: mongoose.Schema.Types.ObjectId, ref: "User", required: true, index: true },
    prediction: { type: Number, required: true }, // 0/1
    probability: { type: Number, default: null },
    message: { type: String, required: true },
    inputs: { type: Object, default: null },
  },
  { timestamps: true }
);

export default mongoose.model("Prediction", predictionSchema);

