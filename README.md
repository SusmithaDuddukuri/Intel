# 🚑 Emergency Response Triage Assistant

## 📌 Overview
I built this project to solve a real problem in emergency care — doctors often need to make quick decisions while dealing with messy or incomplete patient information. Going through all that data takes time, and in emergencies, time is critical.

This application helps by quickly analyzing symptoms and suggesting how serious a patient’s condition might be.

---

## 💡 What This Project Does
The system takes patient symptoms as input and classifies the condition into:
- 🚨 Critical  
- ⚠️ Urgent  
- ✅ Stable  

Based on the result, it also provides simple next-step recommendations so that action can be taken immediately.

---

## ⚙️ How It Works
Instead of using heavy models, I kept the system simple and fast:
- The app reads the symptoms entered by the user  
- It filters and focuses only on relevant keywords  
- Then it matches them with predefined medical conditions  
- Finally, it returns a severity level with suggested actions  

This approach helps reduce unnecessary processing and keeps the response time very low.

---

## 🧠 Approach I Used
The main idea I followed was intelligent filtering:
- Ignore irrelevant or less useful inputs  
- Focus only on important symptoms  
- Make quick decisions using lightweight logic  

This helps simulate context pruning, which is important for reducing latency in real-world systems.

---

## 🛠️ Tech Stack
- Python  
- Streamlit  
- Pandas  
- streamlit-option-menu  

---

## 📊 Features
- Fast symptom-based analysis  
- Simple and clean user interface  
- Severity classification (Critical / Urgent / Stable)  
- Basic insights dashboard  
- Emergency guidelines section  

---

## 🚧 What Didn’t Work
At first, I tried using more complex approaches, but they slowed the system down. Handling noisy or unrelated inputs was also harder than I expected. I realized that keeping the logic simple actually worked better for speed.

---

## 🔮 Future Improvements
- Add machine learning-based triage  
- Improve symptom understanding  
- Include real patient history datasets  
- Optimize for even faster responses  

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 🙌 Final Thoughts
This project helped me understand how important speed and simplicity are in real-world applications. Even a basic system can be useful if it gives quick and clear results.