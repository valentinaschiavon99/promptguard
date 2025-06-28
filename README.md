# 🛡️ PromptGuard
*A Prompt Auditing Framework for LLM Quality Evaluation*  
**Author:** Valentina Schiavon – Matrikelnummer: 12133505  
**Course:** Neuere Methoden in der Computerlinguistik – SS 2025

---

## 🎯 Objective

**PromptGuard** is a modular prototype designed to audit outputs from Large Language Models (LLMs) such as GPT-3.5 and GPT-4.  
It evaluates generated content based on:

- ✅ **Formal Correctness** (structure, punctuation)
- ✅ **Rule Conformity** (keywords and style)
- ✅ **Semantic Similarity** (meaning alignment between prompt and output)

---

## 🧪 How It Works

PromptGuard processes 50 prompt-output pairs and performs:

- Rule-based checks (regex, keyword search)
- Semantic scoring using `sentence-transformers` (free, local embedding model)
- Visualizations with `matplotlib` for result interpretation

---

## 🧰 Technology Stack

- `Python 3.10+`
- `pandas`, `matplotlib`
- `sentence-transformers` (`all-MiniLM-L6-v2`)
- `scikit-learn` (for cosine similarity)

---

## 📁 Structure

📦 promptguard/
├── data/
│ └── prompts_50.csv
├── notebooks/
│ └── PromptGuard.ipynb
├── results/
│ ├── metric_plot.png
│ └── similarity_hist.png
└── README.md


