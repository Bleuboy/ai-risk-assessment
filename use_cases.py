# use_cases.py
use_case_risks = {
    "Consumer App": [
        "Rogue actions",
        "Sensitive Data Disclosure",
        "Excessive Agency",
        "Insecure model output",
        "Prompt Injection",
        "Inferred Sensitive Data",
        "Insecure Plugin Design"
    ],
    "Enterprise App": [
        "Unauthorized Training Data",
        "Model Source Tampering",
        "Rogue actions",
        "Prompt Injection",
        "Sensitive Data Disclosure",
        "Broken Acess Control",
        "Excessive Agency",
        "Insecure model output",
        "Inferred Sensitive Data",
        "Insecure Plugin Design"
    ],
    "Pre-trained Model and Fine-trained Model": [
        "Data Poisoning",
        "Unauthorized Training Data",
        "Model Source Tampering",
        "Rogue actions",
        "Model exfiltration",
        "Prompt Injection",
        "Sensitive Data Disclosure",
        "Broken Acess Control",
        "Excessive Agency",
        "Model theft"
    ],
    "Self-trained model": [
        "Data Poisoning",
        "Unauthorized Training Data",
        "Model Source Tampering",
        "Rogue actions",
        "Model exfiltration",
        "Sensitive Data Disclosure",
        "Broken Acess Control",
        "Excessive Agency",
        "Model theft",
        "Inferred Sensitive Data"
    ]
}


USE_CASES = [
    {"title": "Consumer App", "risks": use_case_risks["Consumer App"]},
    {"title": "Enterprise App", "risks": use_case_risks["Enterprise App"]},
    {"title": "Pre-trained Model and Fine-trained Model", "risks": use_case_risks["Pre-trained Model and Fine-trained Model"]},
    {"title": "Self-trained model", "risks": use_case_risks["Self-trained model"]}
]