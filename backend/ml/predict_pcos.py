import json
import sys
from pathlib import Path

import joblib
import pandas as pd


def load_model_bundle():
    model_path = Path(__file__).resolve().parent / "pcos_model.joblib"
    if not model_path.exists():
        raise FileNotFoundError(
            f"Model not found at {model_path}. Train it first: python3 backend/ml/train_pcos_model.py"
        )
    return joblib.load(model_path)


def read_payload() -> dict:
    if len(sys.argv) < 2:
        raise ValueError(
            "Missing JSON payload argument. Usage: python3 predict_pcos.py '{\"feature\": 1}'"
        )
    return json.loads(sys.argv[1])


def main() -> None:
    bundle = load_model_bundle()
    pipeline = bundle["pipeline"]
    feature_cols = bundle["feature_cols"]

    payload = read_payload()

    row = {c: payload.get(c, 0) for c in feature_cols}
    X = pd.DataFrame([row], columns=feature_cols)

    pred = int(pipeline.predict(X)[0])

    proba = None
    if hasattr(pipeline, "predict_proba"):
        try:
            proba = float(pipeline.predict_proba(X)[0][1])
        except Exception:
            proba = None

    result = {
        "prediction": pred,
        "probability": proba,
        "message": (
            "High PCOS risk. Please consult a doctor / gynecologist."
            if pred == 1
            else "Low PCOS risk. Keep tracking symptoms and maintain a healthy routine."
        ),
    }

    print(json.dumps(result))


if __name__ == "__main__":
    main()
