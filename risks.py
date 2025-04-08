all_risks = [

  {
    "title": "Rogue actions",
    "question": "Do you have safeguards in place to prevent AI from autonomously executing unauthorized actions?",
    "options": [
      "0 = No safeguards in place",
      "1 = Some manual oversight but no automated controls",
      "2 = Limited automated safeguards with human review",
      "3 = Strong safeguards with multi-layered controls",
      "4 = Comprehensive monitoring with real-time anomaly detection and mitigation"
    ],
    "weight" : 1,
    "good" : "Good practice ...",
    "advice": "This involves a model or its components being manipulated to perform unauthorized or harmful actions. This could include malicious actors using the model for unintended purposes, like launching attacks or spreading misinformation. Some Steps that should be implemented to mitigate the Risk: 1-Agent/Plugin Permissions 2-Agent/Plugin User Control"
  },
  {
    "title": "Sensitive Data Disclosure",
    "question": "Do you ensure that AI-generated responses do not expose sensitive or confidential information?",
    "options": [
      "0 = No controls in place",
      "1 = Basic filtering but no systematic oversight",
      "2 = Some automated checks with occasional audits",
      "3 = Strong automated content filtering with human oversight",
      "4 = Comprehensive protection with AI-driven contextual filtering and continuous monitoring"
    ],
    "weight" : 1,
    "good" : "Good practice ...",
    "advice": "<p>This is the unintentional or malicious leakage of sensitive data through the model's output or predictions. "
    "This might happen if the model has memorized personal  information or is susceptible to certain attacks.<br><br><strong> Some Steps that should be implemented to mitigate the Risk:</strong><br>"
    " 1-Privacy Enhancing Technologies<br>2-User Data Management<br>3-Input and Output Validation and Sanitization</p>"
  },
  {
    "title": "Excessive Agency",
    "question": "Do you have safeguards in place to prevent AI systems from autonomously making high-impact decisions without human intervention?",
    "options": [
      "0 = No safeguards in place",
      "1 = Some manual review but no automated controls",
      "2 = Limited automated safeguards with human review",
      "3 = Strong safeguards with multi-layered human-in-the-loop controls",
      "4 = Comprehensive monitoring with real-time intervention and fail-safes"
    ],
    "weight" : 1,
    "good" : "Good practice ...",
    "advice": "<p>Excessive agency occurs when an LLM system is given too much autonomy and performs unexpected, potentially harmful actions. Causes are excessive functions, authorisations or autonomy. This can result in security risks for confidentiality, integrity and availability"
    "<br><br><strong> Some Steps that should be implemented to mitigate the Risk:</strong><br>"
    "1-Limit plugins/tools to essential functions "
    "only<br>2-use specific tools instead of broad commands,<br>3-grant only necessary access<br>4-implement approvals for critical operations</p>"
  },
  {
    "title": "Insecure model output",
    "question": "Do you have filtering mechanisms in place to prevent the AI from generating malicious, misleading, or harmful outputs?",
    "options": [
      "0 = No filtering or output controls in place",
      "1 = Basic manual review but no systematic filtering",
      "2 = Some automated filtering with occasional audits",
      "3 = Robust automated content filtering with human oversight",
      "4 = Comprehensive AI-driven filtering with continuous monitoring and real-time mitigation"
    ],
    "advice": "<p>Refers to outputs from the model that might be unsafe, misleading, or easily manipulated, "
    "which can have harmful consequences, especially when the model is used in safety-critical applications.<br><br><strong> Some Steps that should be implemented "
    "to mitigate the Risk:</strong><br>"
    "1-Output Validation and Sanitization<br>2-Block, nullify, or sanitize insecure output from AI models before passing it to applications, extensions or users.</p>"
  },
  {
    "title": "Prompt Injection",
    "question": "Do you validate and sanitize user inputs to prevent prompt injection attacks?",
    "options": [
      "0 = No input validation",
      "1 = Basic input validation",
      "2 = Automated input validation with manual review",
      "3 = Advanced input validation with anomaly detection",
      "4 = AI-driven validation and contextual filtering with continuous monitoring"
    ],
    "weight" : 1,
    "good" : "Good practice ...",
    "advice": "<p>Involves manipulating or crafting inputs (prompts) to trick a language model into producing unintended or malicious outputs. "
    "This is often seen in AI systems with generative capabilities, such as chatbots.<br><br><strong> Some Steps that should be implemented to mitigate the Risk:</strong><br>1-Input "
    "Validation and Sanitization<br>2-Adversarial Training and Testing</p>"
  },
  {
    "title": "Inferred Sensitive Data",
    "question": "Do you prevent AI from unintentionally inferring and exposing confidential information?",
    "options": [
      "0 = No controls or monitoring in place",
      "1 = Basic manual review, no systematic oversight",
      "2 = Automated detection of sensitive inference with limited audits",
      "3 = Strong automated monitoring with human review and filtering",
      "4 = Comprehensive AI-driven inference detection with continuous monitoring and real-time mitigation"
    ],
    "advice": "<p>This refers to the extraction of sensitive or private data through indirect means. Attackers may use the outputs "
    "of a model to infer confidential information that wasn’t explicitly part of the training data.<br><br><strong> Some Steps that should be implemented to mitigate the Risk:</strong><br>"
    "1-Training Data Management<br>2-Output Validation and Sanitization</p>"
  },
  {
    "title": "Insecure Plugin Design",
    "question": "Do you perform security audits and code reviews for third-party plugins before integrating them into your AI systems?",
    "options": [
      "0 = No review or audit of third-party plugins",
      "1 = Basic manual review without formal process",
      "2 = Periodic audits and selective code reviews",
      "3 = Systematic security audits and thorough code reviews before integration",
      "4 = Comprehensive continuous auditing, monitoring, and sandbox testing of all plugins"
    ],
    "weight" : 1,
    "good" : "Good practice ...",
    "advice": "<p>A lack of security controls being integrated into the application throughout the development cycle. <br><br><strong> Some Steps that should be implemented to mitigate the Risk:</strong><br>"
    "1-Conduct security assessments on third-party integrations<br>2-Enforce API access controls to prevent vulnerabilities.</p>"
  },
  {
    "title": "Unauthorized Training Data",
    "question": "Do you ensure compliance with data governance policies when sourcing training data for your AI models?",
    "options": [
      "0 = No compliance checks",
      "1 = Some compliance checks",
      "2 = Regular compliance checks with basic tracking",
      "3 = Strong governance processes with documented compliance",
      "4 = Full compliance with automated tracking, documentation, and audits"
    ],
    "weight" : 1,
    "good" : "Good practice ...",
    "advice": "<p>This refers to the inclusion of data in the model's training set that wasn't  authorized or "
    "is not properly vetted, potentially violating privacy or ethical guidelines.<br><br><strong> Some Steps that should be implemented to mitigate the Risk:</strong><br>"
    "1-Training Data Management<br>2-Ensure that all data used to train and evaluate models is authorized for the intended purposes.</p>"
  },
  {
    "title": "Model Source Tampering",
    "question": "Do you have control and integrity-checking mechanisms to detect unauthorized model modifications?",
    "options": [
      "0 = No integrity checks",
      "1 = Basic integrity checks during development",
      "2 = Automated integrity validation at release points",
      "3 = Continuous integrity monitoring and alerts",
      "4 = Full chain-of-custody verification and continuous integrity monitoring"
    ],
    "advice": "<p>This threat involves altering the source code or model architecture itself to either "
    "degrade performance, leak information, or create vulnerabilities for further exploitation.<br><br><strong> Some Steps that should be implemented to mitigate the Risk:</strong><br>"
    "1-Secure-by-Default ML Tooling<br>2-Model and Data Integrity Management<br>3-Model"
    " and Data Access Controls<br>4-Model and Data Inventory Management</p>"
  },
  {
    "title": "Broken Acess Control",
    "question": "Do you have access controls in place to restrict unauthorized modifications to AI models and datasets?",
    "options": [
      "0 = No access controls implemented",
      "1 = Basic access restrictions but no logging or enforcement",
      "2 = Role-based access control with limited monitoring",
      "3 = Granular access control with audit logs and alerts",
      "4 = Highly secure access control with continuous monitoring and real-time threat detection"
    ],
    "weight" : 1,
    "good" : "Good practice ...",
    "advice":"<p>Broken Access Control tritt auf, wenn Sicherheitsmechanismen "
    "nicht korrekt umgesetzt sind, sodass unbefugte Benutzer auf geschützte Daten oder Funktionen zugreifen "
    "können.<br><br><strong> Some Steps that should be implemented to mitigate the Risk:</strong><br>Enforce multi-factor authentication and role-based access control</span> to secure AI environments.</p>"

  },
  {
    "title": "Data Poisoning",
    "question": "Do you have measures in place to verify the integrity and authenticity of your AI training data?",
    "options": [
      "0 = No measures in place",
      "1 = Basic checks but no formal verification process",
      "2 = Some automated integrity verification steps",
      "3 = Comprehensive integrity verification with periodic audits",
      "4 = Rigorous integrity checks with continuous monitoring and anomaly detection"
    ],
    "weight" : 1,
    "good" : "Good practice ...",
    "advice": "<p>This occurs when malicious actors inject harmful data into the training set of a machine learning model "
    "to degrade its performance or manipulate its behavior. <br><br><strong> Some Steps that should be implemented to mitigate the Risk:</strong><br>1-Training "
    "Data Sanitization<br>2-Secure-by-Default ML Tooling<br>3-Model and Data Integrity Management<br>4-Model and Data Access Control</p>"
  },
  {
    "title": "Model exfiltration",
    "question": "Do you monitor and prevent unauthorized attempts to download, copy, or steal your AI models?",
    "options": [
      "0 = No monitoring in place",
      "1 = Minimal monitoring with basic logging",
      "2 = Periodic security audits but limited real-time detection",
      "3 = Active monitoring with alerts for suspicious access attempts",
      "4 = Advanced real-time threat detection with strict access control measures"
    ],
    "weight" : 1,
    "good" : "Good practice ...",
    "advice": "<p>This is when a trained machine learning model is illicitly extracted from a system to be used for unauthorized purposes, often"
    " in ways that bypass security or intellectual property protections.<br><br><strong> Some Steps that should be implemented to mitigate the Risk:</strong><br>"
    "1-Model and Data Inventory Management<br>2-Model and Data Access Controls<br>3-Model and Data Integrity Management<br>4-Secure-by-Default ML Tooling</p>"
  },
  {
    "title": "Model theft",
    "question": "Do you implement API rate limiting and access controls to prevent unauthorized extraction of your AI models?",
    "options": [
      "0 = No rate limiting or access controls in place",
      "1 = Basic API restrictions but no monitoring",
      "2 = API rate limiting with limited monitoring",
      "3 = Granular API access control with audit logs and alerts",
      "4 = Advanced rate limiting, continuous monitoring, and real-time detection of extraction attempts"
    ],
    "weight" : 1,
    "good" : "Good practice ...",
    "advice": "<p> The theft of LLM models by hackers or APTs endangers intellectual property "
    "and can cause economic damage, loss of reputation and unauthorised use.<br><br><strong> Some Steps that should be implemented to mitigate the Risk:</strong><br>"
    "1-Deploy encryption, watermarking<br>2-Secure enclaves to protect proprietary AI models from unauthorized use.</p>"
  }
]