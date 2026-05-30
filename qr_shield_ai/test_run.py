from nlp_engine import analyze_text_payload
import json

test_string = "URGENT: Your PayPal account is restricted. Verify your OTP immediately to avoid suspension."
result = analyze_text_payload(test_string)
print(json.dumps(result, indent=2))