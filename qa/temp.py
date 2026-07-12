def classify_temp(temp):
    if 18 <= temp <= 30:
        return "VALID"
    elif 30 < temp:
        return "HIGH_TEMP"
    else:
        return "LOW_TEMP"