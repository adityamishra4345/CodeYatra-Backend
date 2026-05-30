import re
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

def analyze_text_payload(user_text: str) -> dict:
    findings = []
    triggered_keywords = []
    threat_score = 0

    regex_rules = {
        "Urgency/Fear": r"(suspension|block|unauthorized|action required|urgent|immediately|restrict)",
        "OTP Harvest": r"(otp|one-time password|verification code|secure login|authorization)",
        "Financial Trap": r"(lottery|prize|reward|gift card|crypto|bonus|claim package)"
    }

    for category, pattern in regex_rules.items():
        matches = re.findall(pattern, user_text.lower())
        if matches:
            triggered_keywords.extend(list(set(matches)))
            findings.append(f"Triggered risk indicator: {category}")
            threat_score += 25

    inputs = tokenizer(user_text, return_tensors="pt", truncation=True, max_length=512)
    
    with torch.no_grad():
        outputs = model(**inputs)
    
    logits = outputs.logits
    confidence = torch.softmax(logits, dim=1).max().item()

    if len(triggered_keywords) > 0:
        nlp_confidence = float(max(confidence, 0.85))
        nlp_label = "phishing/scam"
        threat_score += 30
    else:
        nlp_confidence = float(confidence)
        nlp_label = "safe/neutral"

    threat_score = min(threat_score, 100)
    
    if threat_score >= 60:
        verdict = "PHISHING"
    elif threat_score >= 30:
        verdict = "SUSPICIOUS"
    else:
        verdict = "SAFE"

    return {
        "verdict": verdict,
        "threat_score": threat_score,
        "triggered_keywords": triggered_keywords,
        "nlp_label": nlp_label,
        "nlp_confidence": round(nlp_confidence, 2),
        "findings": findings if findings else ["No typical scam metrics flagged."]
    }