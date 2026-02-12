def predict_severity(input_value):
    if input_value.lower() in ["high", "severe", "critical"]:
        return "High"
    elif input_value.lower() in ["medium", "moderate"]:
        return "Medium"
    else:
        return "Low"