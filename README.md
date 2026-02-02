# PromptGuard – LLM Output Auditing System

PromptGuard is a lightweight auditing framework designed to evaluate Large Language Model (LLM) outputs by combining:

- Semantic similarity using sentence embeddings  
- Rule-based heuristics  
- Risk scoring  

It supports both batch evaluation and real-time integration via a REST API.

---

## 🚀 Features

- Semantic analysis of prompt–output pairs using NLP embeddings  
- Risk estimation based on multiple metrics  
- CLI tool for batch auditing (CSV input)  
- FastAPI service for real-time auditing  
- JSON reports for downstream analysis  

---

## 📂 Project Structure

promptguard/
│
├── promptguard/
│   ├── audit.py          # Core audit logic
│   ├── embeddings.py    # Semantic similarity engine
│   ├── checks.py        # Rule-based checks
│   ├── cli.py           # Batch audit CLI
│   └── api/
│       └── main.py      # FastAPI service
│
├── notebooks/
│   └── promptguard_demo.ipynb
│
├── requirements.txt
└── README.md

---

## ⚙️ Installation

Create and activate a virtual environment:

python -m venv .venv  
source .venv/bin/activate  

Install dependencies:

pip install -r requirements.txt  

(or using uv if preferred)

---

## 🧪 Quick Test

python -c "from promptguard.audit import audit_one; print(audit_one('Say hi','Hello!'))"

---

## 🖥 CLI Usage (Batch Auditing)

python -m promptguard.cli audit \
  -i data.csv \
  -o results/report.json

Options:

--limit : limit number of rows  
--prompt-col : prompt column name  
--output-col : output column name  

---

## 🌐 REST API

Start the API server:

python -m uvicorn promptguard.api.main:app --reload

Open Swagger UI:

http://127.0.0.1:8000/docs

---

### Example request

{
  "prompt": "Say hi",
  "output": "Hello!"
}

### Example response

{
  "prompt": "Say hi",
  "output": "Hello!",
  "scores": {
    "semantic_similarity": 0.74,
    "rule_conformity": 0.7,
    "risk": 0.26
  },
  "flags": ["too_short"]
}

---

## 🧠 How It Works

1. Prompts and outputs are encoded using sentence embeddings  
2. Semantic similarity is computed  
3. Rule-based checks evaluate output quality  
4. A combined risk score is produced  

This allows detection of:

- Unrelated or hallucinated outputs  
- Low-quality responses  
- Potentially risky generations  

---

## 📌 Use Cases

- LLM safety auditing  
- Quality monitoring pipelines  
- AI output validation  
- Research experiments  

---

## 📈 Future Improvements

- Configurable risk thresholds  
- Authentication for API  
- Async batch processing  
- Monitoring dashboards  

---

## 👩‍💻 Author

Valentina Schiavon

