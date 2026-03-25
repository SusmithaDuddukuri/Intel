# 🚑 Emergency Triage Assistant

## 📌 Overview

The **Emergency Triage Assistant** is a Streamlit-based application designed to assist medical professionals in emergency rooms and disaster scenarios. It analyzes patient symptoms and classifies them into severity levels to support quick decision-making.

---

## 🚨 Problem Statement

In emergency situations:

* Medical staff deal with **unstructured and messy patient data**
* Critical decisions must be made within **seconds**
* Delays can lead to **serious consequences or loss of life**

---

## 💡 Solution

This project provides:

* ⚡ **Real-time symptom analysis**
* 🧠 **Keyword-based triage classification**
* 🚨 **Severity categorization (Critical / Urgent / Stable)**
* 📊 **Insights dashboard for monitoring cases**

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Pandas
* Streamlit Option Menu

---

## 📂 Project Structure

```
CHALLENGE-3-EMERGENCY-TRIAGE-ASSISTANT/
│
├── app.py                     # Main Streamlit application
├── requirements.txt          # Dependencies
├── README.md                 # Documentation
│
└── modules/
    ├── triage_engine.py      # Core triage logic
    └── triage_logic.py       # Alternative triage logic
```

---

## ⚙️ How It Works

1. User selects a **primary symptom**
2. Adds **additional symptoms**
3. System processes input using keyword-based logic
4. Outputs:

   * Severity Level (Critical / Urgent / Stable)
   * Recommended actions

---

## 🧠 Triage Logic

### Critical Conditions

* Heart attack
* Cardiac arrest
* Severe bleeding
* Stroke
* Unconsciousness
* Difficulty breathing

### Urgent Conditions

* Chest pain
* High fever
* Vomiting
* Severe headache
* Abdominal pain

---

## 🚀 How to Run

### 1. Clone Repository

```
git clone <your-repo-link>
cd CHALLENGE-3-EMERGENCY-TRIAGE-ASSISTANT
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Run Application

```
streamlit run app.py
```

---

## 📊 Features

* 🏠 Home Page with problem & solution
* ⚙️ Services Overview
* 🧪 Symptom Analyzer
* 🚨 Severity Classification
* 📈 Insights Dashboard
* 📋 Emergency Guidelines

---

## ⚠️ Limitations

* Uses **keyword-based logic** (not ML/AI model)
* Does not process **large medical datasets**
* No real-time hospital integration

---

## 🔮 Future Improvements

* Add **Intelligent Context Pruning**
* Integrate **LLM or NLP models**
* Connect with **real patient databases**
* Add **voice input support**
* Improve **accuracy using ML**
* Add **ML-based triage model**

---

## 👩‍💻 Author

Developed as part of an Intel Challenge-3 project.

---

## 📜 License

This project is for educational purposes only.