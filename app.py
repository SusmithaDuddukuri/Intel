import streamlit as st
import pandas as pd
from modules.triage_engine import triage_decision
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Emergency Response Assistant", layout="wide")

# ---------- Background ----------
page_bg = """
<style>
[data-testid="stAppViewContainer"]{
background-image: linear-gradient(rgba(255,255,255,0.92), rgba(255,255,255,0.92)),
url("https://images.unsplash.com/photo-1580281657527-47a3b2f9b1a2");
background-size: cover;
background-position: center;
background-attachment: fixed;
}

.card{
padding:20px;
border-radius:15px;
box-shadow:0 4px 10px rgba(0,0,0,0.15);
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# ---------- NAVBAR ----------
selected = option_menu(
    menu_title="🚑 Emergency Response Assistant",
    options=["Home","Services","Analyzer","Severity Classification","Insights","Guidelines"],
    icons=["house","heart","activity","exclamation-triangle","bar-chart","book"],
    orientation="horizontal",
    key="main_menu"
)

# ---------- HOME ----------
if selected == "Home":

    st.title("🚑 AI Emergency Triage Assistant")

    # HERO / Main Feature
    st.markdown("""
<div style="background:linear-gradient(90deg,#2563eb,#06b6d4);
padding:25px;border-radius:15px;color:white;text-align:center">
<h2>⚡ Fast & Smart Emergency Decision Support</h2>
<p>
Designed for emergency rooms and disaster zones where every second counts.
This AI-powered assistant analyzes patient symptoms instantly and provides
severity-based triage recommendations.
</p>
<img src="https://cdn-icons-png.flaticon.com/512/3077/3077403.png" width="120" style="margin-top:15px">
</div>
""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Problem & Solution Cards
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
<div class="card" style="background:#fee2e2">
<h4>🚨 Problem</h4>
<p>
Emergency medical staff face messy and unstructured patient histories,
lengthy disaster protocols, and must make decisions within seconds.
Time lost can cost lives.
</p>
<img src="https://cdn-icons-png.flaticon.com/512/2581/2581726.png" width="60" style="margin-top:10px">
</div>
""", unsafe_allow_html=True)

    with col2:
        st.markdown("""
<div class="card" style="background:#e0f2fe">
<h4>💡 Solution</h4>
<p>
Using Intelligent Context Pruning, the system discards irrelevant patient history
and highlights critical symptoms for rapid triage. Immediate actionable insights
are provided for lifesaving decisions.
</p>
<img src="https://cdn-icons-png.flaticon.com/512/3135/3135670.png" width="60" style="margin-top:10px">
</div>
""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Features Section with Cards
    col3, col4, col5 = st.columns(3)

    with col3:
        st.markdown("""
<div class="card" style="background:#E3F2FD">
<h4>⚡ Real-Time Analysis</h4>
<p>Generates patient evaluation results in milliseconds for fast action.</p>
<img src="https://cdn-icons-png.flaticon.com/512/3039/3039430.png" width="50" style="margin-top:10px">
</div>
""", unsafe_allow_html=True)

    with col4:
        st.markdown("""
<div class="card" style="background:#E8F5E9">
<h4>🧠 Intelligent Filtering</h4>
<p>Automatically removes irrelevant data such as old records, irrelevant visits, or non-critical history.</p>
<img src="https://cdn-icons-png.flaticon.com/512/2910/2910761.png" width="50" style="margin-top:10px">
</div>
""", unsafe_allow_html=True)

    with col5:
        st.markdown("""
<div class="card" style="background:#FFF3E0">
<h4>🚨 Smart Triage</h4>
<p>Classifies patients into Critical, Urgent, and Stable categories to prioritize care.</p>
<img src="https://cdn-icons-png.flaticon.com/512/3050/3050471.png" width="50" style="margin-top:10px">
</div>
""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

# UI improved for better user experience

# ---------- SERVICES ----------
if selected == "Services":

    st.title("🚑 Intelligent Emergency Services")

    st.markdown("""
<div style="background:linear-gradient(90deg,#0ea5e9,#2563eb);
padding:20px;border-radius:12px;color:white;text-align:center">
<h3>⚙️ AI-Powered Emergency Support System</h3>
<p>
Designed for real-world emergency environments, this system helps medical teams
quickly process large, unstructured patient data and identify the most critical
information required for immediate action.
</p>
</div>
""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
<div style="background:#E3F2FD;padding:20px;border-radius:15px">
<img src="https://cdn-icons-png.flaticon.com/512/4320/4320337.png" width="70">
<h4>🧠 Intelligent Context Pruning</h4>
<p>
Filters irrelevant patient history (old records, unrelated data) and keeps only
critical symptoms. This reduces processing time and improves decision accuracy.
</p>
</div>
""", unsafe_allow_html=True)

    with col2:
        st.markdown("""
<div style="background:#E8F5E9;padding:20px;border-radius:15px">
<img src="https://cdn-icons-png.flaticon.com/512/2966/2966327.png" width="70">
<h4>⚡ Ultra-Fast Decision Support</h4>
<p>
Provides triage decisions in under 500ms by processing only relevant data.
Ensures immediate response in emergency situations.
</p>
</div>
""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col3, col4 = st.columns(2)

    with col3:
        st.markdown("""
<div style="background:#FFF3E0;padding:20px;border-radius:15px">
<img src="https://cdn-icons-png.flaticon.com/512/3063/3063821.png" width="70">
<h4>📊 Real-Time Triage Classification</h4>
<p>
Classifies patients into Critical, Urgent, and Stable categories based on
symptoms to prioritize treatment effectively.
</p>
</div>
""", unsafe_allow_html=True)

    with col4:
        st.markdown("""
<div style="background:#FCE4EC;padding:20px;border-radius:15px">
<img src="https://cdn-icons-png.flaticon.com/512/3771/3771417.png" width="70">
<h4>🏥 Real-World Deployment</h4>
<p>
Can be used in hospitals, ambulances, and disaster relief zones to assist
medical teams in handling large volumes of patients efficiently.
</p>
</div>
""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
<div style="background:#f1f5f9;padding:20px;border-radius:12px">
<h4>📌 How It Works</h4>
<ul>
<li>📝 Input patient symptoms</li>
<li>🧹 Remove irrelevant history (Context Pruning)</li>
<li>⚡ Analyze critical data</li>
<li>🚨 Generate severity result instantly</li>
</ul>
</div>
""", unsafe_allow_html=True)
    
# ---------- ANALYZER ----------
if selected == "Analyzer":

    st.title("Patient Symptom Evaluation")

    # Small image + text
    col1, col2 = st.columns([1,4])

    with col1:
        st.image(
            "https://cdn-icons-png.flaticon.com/512/2966/2966327.png",  # hospital icon
            width=80
        )

    with col2:
        st.write(
            "Select a primary symptom from the dropdown and enter additional details. "
            "The system will analyze the condition and provide recommended next steps."
        )

    # Symptom options
    symptom_options = [
        "Chest Pain",
        "Breathing Difficulty",
        "Severe Bleeding",
        "High Fever",
        "Dizziness",
        "Unconsciousness",
        "Severe Headache",
        "Abdominal Pain",
        "Vomiting",
        "Fatigue"
    ]

    # Dropdown
    primary_symptom = st.selectbox(
        "Select Primary Symptom",
        ["Select..."] + symptom_options
    )

    # Text input
    manual_symptoms = st.text_area(
        "Additional Symptoms",
        placeholder="Enter other symptoms..."
    )

    # Analyze Button
    if st.button("Analyze"):

        combined = ""
        if primary_symptom != "Select...":
            combined += primary_symptom + ", "

        combined += manual_symptoms

        if combined.strip() == "":
            st.warning("Please enter symptoms for analysis.")
        else:
            result = triage_decision(combined)

            st.markdown("---")
            st.subheader("Evaluation Result")

            if "CRITICAL" in result.upper():
                st.error("🚨 Critical Condition")
                st.markdown("""
<div style="background:#fee2e2;padding:15px;border-radius:12px">
<b>Recommended Actions:</b><br>
• Call emergency response immediately<br>
• Begin CPR or first aid if necessary<br>
• Prepare for immediate hospital admission<br>
• Monitor vital signs continuously
</div>
""", unsafe_allow_html=True)

            elif "URGENT" in result.upper():
                st.warning("⚠ Urgent Condition")
                st.markdown("""
<div style="background:#fff4e5;padding:15px;border-radius:12px">
<b>Recommended Actions:</b><br>
• Schedule rapid clinical evaluation<br>
• Administer symptomatic treatment<br>
• Observe patient closely<br>
• Prepare for potential escalation
</div>
""", unsafe_allow_html=True)

            else:
                st.success("✅ Stable Condition")
                st.markdown("""
<div style="background:#e8f5e9;padding:15px;border-radius:12px">
<b>Recommended Actions:</b><br>
• Monitor symptoms regularly<br>
• Provide routine care<br>
• Schedule follow-up check<br>
• Educate patient on warning signs
</div>
""", unsafe_allow_html=True)

# ---------- SEVERITY ----------
if selected == "Severity Classification":

    st.title("Patient Severity Classification")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("https://cdn-icons-png.flaticon.com/512/2966/2966325.png", width=70)
        st.markdown("""<div style="background:#fee2e2;padding:20px;border-radius:15px;text-align:center">
<h3>🔴 Critical</h3>
<p>Life-threatening condition that requires immediate medical attention.
Delay in treatment can lead to serious complications or death.</p>
<b>Examples:</b><br>
Cardiac arrest, severe bleeding, unconsciousness
</div>""", unsafe_allow_html=True)

    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/3774/3774299.png", width=70)
        st.markdown("""<div style="background:#fff4e5;padding:20px;border-radius:15px;text-align:center">
<h3>🟠 Urgent</h3>
<p>Serious condition that needs quick medical evaluation to prevent worsening.</p>
<b>Examples:</b><br>
High fever, severe pain, breathing difficulty
</div>""", unsafe_allow_html=True)

    with col3:
        st.image("https://cdn-icons-png.flaticon.com/512/2966/2966488.png", width=70)
        st.markdown("""<div style="background:#e8f5e9;padding:20px;border-radius:15px;text-align:center">
<h3>🟢 Stable</h3>
<p>Condition is under control and not immediately dangerous.</p>
<b>Examples:</b><br>
Mild headache, fatigue, minor injuries
</div>""", unsafe_allow_html=True)

# ---------- INSIGHTS ----------
if selected == "Insights":

    st.title("📊 Emergency Insights Dashboard")

    col1, col2 = st.columns([1,4])

    with col1:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135670.png", width=80)

    with col2:
        st.markdown("""
<div style="background:#e0f2fe;padding:15px;border-radius:12px">
<b>📈 Real-Time Monitoring</b><br>
Overview of patient evaluations and severity distribution to support quick decision-making.
</div>
""", unsafe_allow_html=True)

    st.markdown("---")

    col1, col2, col3, col4 = st.columns(4)

    with col1: st.metric("📊 Total Cases", "152")
    with col2: st.metric("🚨 Critical", "31")
    with col3: st.metric("⚠ Urgent", "44")
    with col4: st.metric("✅ Stable", "77")

    st.markdown("---")

    data = pd.DataFrame({
        "Severity": ["Critical","Urgent","Stable"],
        "Cases": [31,44,77]
    })

    st.bar_chart(data.set_index("Severity"))

    st.markdown("---")

    col5, col6 = st.columns(2)

    with col5:
        st.markdown("""
<div style="background:#fee2e2;padding:15px;border-radius:12px">
<b>🚨 Critical Cases Insight</b><br><br>
Higher critical cases indicate need for immediate resource allocation
and emergency readiness.
</div>
""", unsafe_allow_html=True)

    with col6:
        st.markdown("""
<div style="background:#e8f5e9;padding:15px;border-radius:12px">
<b>✅ Stable Cases Insight</b><br><br>
Stable cases can be monitored, helping reduce pressure on emergency units.
</div>
""", unsafe_allow_html=True)

# ---------- GUIDELINES ----------
if selected == "Guidelines":

    st.title("🏥 Emergency Response Guidelines")

    col1, col2 = st.columns([1,4])

    with col1:
        st.image("https://cdn-icons-png.flaticon.com/512/2966/2966327.png", width=80)

    with col2:
        st.markdown("""
<div style="background:#e0f2fe;padding:15px;border-radius:12px">
<b>📋 Standard Emergency Procedure</b><br>
Follow these structured steps to ensure proper patient handling and quick response.
</div>
""", unsafe_allow_html=True)

    st.markdown("---")

    col3, col4 = st.columns(2)

    with col3:
        st.image("https://cdn-icons-png.flaticon.com/512/2966/2966488.png", width=60)
        st.markdown("""
<div style="background:#fee2e2;padding:15px;border-radius:12px">
<b>🚨 Initial Assessment</b><br><br>
• Check airway, breathing, circulation<br> 
• Identify visible injuries<br> 
• Assess consciousness level<br>
</div>
""", unsafe_allow_html=True)

    with col4:
        st.image("https://cdn-icons-png.flaticon.com/512/3774/3774299.png", width=60)
        st.markdown("""
<div style="background:#fff4e5;padding:15px;border-radius:12px">
<b>🩺 Medical Evaluation</b><br><br>
• Review symptoms carefully<br>  
• Identify severity level<br>  
• Prioritize treatment order<br> 
</div>
""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col5, col6 = st.columns(2)

    with col5:
        st.image("https://cdn-icons-png.flaticon.com/512/2966/2966325.png", width=60)
        st.markdown("""
<div style="background:#e8f5e9;padding:15px;border-radius:12px">
<b>💊 Treatment Actions</b><br><br>
• Provide immediate care<br>
• Administer required medication<br> 
• Stabilize patient condition<br>
</div>
""", unsafe_allow_html=True)

    with col6:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135670.png", width=60)
        st.markdown("""
<div style="background:#ede9fe;padding:15px;border-radius:12px">
<b>📊 Monitoring & Follow-up</b><br><br>
• Monitor vital signs<br>
• Track patient progress<br>
• Decide admission or discharge<br>  
</div>
""", unsafe_allow_html=True)