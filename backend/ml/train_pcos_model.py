import json
import os
from pathlib import Path

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def project_root() -> Path:
    return Path(__file__).resolve().parents[2]


def load_merged_dataset() -> pd.DataFrame:
    root = project_root()
    wo_path = root / "PCOS_data_without_infertility (1).xlsx"
    inf_path = root / "PCOS_infertility.csv"

    if not wo_path.exists():
        raise FileNotFoundError(f"Missing dataset file: {wo_path}")
    if not inf_path.exists():
        raise FileNotFoundError(f"Missing dataset file: {inf_path}")

    df_wo = pd.read_excel(wo_path)
    df_inf = pd.read_csv(inf_path)

    df = pd.merge(
        df_wo,
        df_inf,
        on="Patient File No.",
        suffixes=("", "_y"),
        how="left",
    )

    # Drop duplicate columns from merge
    drop_cols = [
        "Unnamed: 41",
        "Sl. No_y",
        "PCOS (Y/N)_y",
        "  I   beta-HCG(mIU/mL)_y",
        "II    beta-HCG(mIU/mL)_y",
        "AMH(ng/mL)_y",
        "Patient File No.",
        "Sl. No",
        "  I   beta-HCG(mIU/mL)",
        "II    beta-HCG(mIU/mL)",
        "AMH(ng/mL)",
        "TSH (mIU/L)",
        "PRL(ng/mL)",
        "Vit D3 (ng/mL)",
        "PRG(ng/mL)",
        "RBS(mg/dl)",
        "Follicle No. (L)",
        "Follicle No. (R)",
        "Endometrium (mm)",
        "Hb(g/dl)",
        "Avg. F size (L) (mm)",
        "Avg. F size (R) (mm)",
        "RR (breaths/min)",
        "BP _Systolic (mmHg)",
        "BP _Diastolic (mmHg)",
    ]
    df = df.drop(columns=[c for c in drop_cols if c in df.columns], errors="ignore")

    return df


def main() -> None:
    root = project_root()

    # Use the same feature set as data.xlsx (aligns with the web form fields)
    feature_cols = [
        " Age (yrs)",
        "Weight (Kg)",
        "Height(Cm) ",
        "BMI",
        "Blood Group",
        "Pulse rate(bpm) ",
        "Cycle(R/I)",
        "Cycle length(days)",
        "Marraige Status (Yrs)",
        "Pregnant(Y/N)",
        "No. of aborptions",
        "Hip(inch)",
        "Waist(inch)",
        "Waist:Hip Ratio",
        "Weight gain(Y/N)",
        "hair growth(Y/N)",
        "Skin darkening (Y/N)",
        "Hair loss(Y/N)",
        "Pimples(Y/N)",
        "Fast food (Y/N)",
        "Reg.Exercise(Y/N)",
    ]
    target_col = "PCOS (Y/N)"

    df = load_merged_dataset()

    missing = [c for c in feature_cols + [target_col] if c not in df.columns]
    if missing:
        raise ValueError(
            "Dataset is missing expected columns: " + ", ".join(missing)
        )

    X = df[feature_cols]
    y = df[target_col]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
            (
                "model",
                RandomForestClassifier(
                    n_estimators=300,
                    random_state=42,
                    class_weight="balanced",
                ),
            ),
        ]
    )

    pipeline.fit(X_train, y_train)

    y_pred = pipeline.predict(X_test)
    acc = float(accuracy_score(y_test, y_pred))
    cm = confusion_matrix(y_test, y_pred).tolist()
    report = classification_report(y_test, y_pred, output_dict=True)

    out_dir = Path(__file__).resolve().parent
    model_path = out_dir / "pcos_model.joblib"
    metrics_path = out_dir / "pcos_metrics.json"

    joblib.dump(
        {
            "pipeline": pipeline,
            "feature_cols": feature_cols,
            "target_col": target_col,
        },
        model_path,
    )

    metrics = {
        "accuracy": acc,
        "confusion_matrix": cm,
        "classification_report": report,
        "n_rows": int(df.shape[0]),
        "n_features": int(len(feature_cols)),
        "model_path": str(model_path),
    }

    metrics_path.write_text(json.dumps(metrics, indent=2))

    print(f"Saved model: {model_path}")
    print(f"Saved metrics: {metrics_path}")
    print(f"Accuracy: {acc:.4f}")


if __name__ == "__main__":
    main()
