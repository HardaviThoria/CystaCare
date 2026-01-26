# Machine Learning Models



## Planned Models

### 1. PCOS Risk Prediction Model
- **Algorithm:** Random Forest Classifier
- **Library:** Scikit-learn
- **Target Accuracy:** 83%+
- **Features:** 29+ health parameters
- **Output:** Risk score (0-1) + recommendations

### 2. Sentiment Analysis Model
- **Library:** text2emotion or Huggingface
- **Emotions:** Happy, Sad, Angry, Fear, Surprise
- **Input:** Journal text
- **Output:** Emotion percentages

---

## Planned Structure

```
ml-models/
├── data/
│   ├── raw/
│   │   ├── PCOS_data.xlsx
│   │   └── PCOS_infertility.csv
│   ├── processed/
│   │   └── cleaned_data.csv
│   └── README.md
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_model_training.ipynb
│   └── 03_evaluation.ipynb
├── models/
│   ├── pcos_classifier.pkl
│   └── scaler.pkl
├── scripts/
│   ├── train_model.py
│   ├── predict.py
│   └── sentiment_analysis.py
└── README.md (this file)
```

---

## Development Timeline

- **next:** Data collection and preprocessing
- **next:** Model training and evaluation
- **Integration:** Connect with backend via python-shell

---

## Datasets

### Primary Dataset
- **Source:** Kaggle / Research papers
- **Size:** 500+ samples
- **Features:** Age, BMI, symptoms, lifestyle factors
- **Target:** PCOS diagnosis (binary)
OR
### Custom Dataset
- **Collection Method:** Google Forms survey
- **Status:** Data collection planned
- **Purpose:** Improve model with diverse data

---

## Evaluation Metrics

- **Accuracy:** Primary metric (target: 83%+)
- **Precision:** Minimize false positives
- **Recall:** Minimize false negatives
- **F1-Score:** Balance precision and recall
- **ROC-AUC:** Overall model performance

---

**Current Phase:** Architecture Planning  
**Next Milestone:** Begin data collection

