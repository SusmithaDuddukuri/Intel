def triage_decision(symptoms):

    text = symptoms.lower()

    critical_keywords = [
        "chest pain",
        "heart attack",
        "unconscious",
        "severe bleeding",
        "cardiac arrest",
        "difficulty breathing",
        "stroke"
    ]

    urgent_keywords = [
        "high fever",
        "vomiting",
        "fracture",
        "severe headache",
        "dizziness",
        "abdominal pain"
    ]

    for word in critical_keywords:
        if word in text:
            return "CRITICAL - Immediate medical attention required."

    for word in urgent_keywords:
        if word in text:
            return "URGENT - Patient should be evaluated quickly."

    return "STABLE - Monitor the patient condition."