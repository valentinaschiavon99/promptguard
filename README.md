# 🔐 PromptGuard – LLM Prompt Risk Analyzer

**PromptGuard** is a modular, auditable tool for evaluating prompts submitted to Large Language Models (LLMs) like GPT-4. It was developed by **Valentina Schiavon** as part of the course  
🧠 *Neuere Methoden in der Computerlinguistik (510.607, 25S)*  
at **Alpen-Adria-Universität Klagenfurt**.

## 🎯 Project Objective

PromptGuard detects and scores potential risks in user-written prompts—such as:
- 🧪 **Prompt Injection**
- ⚠️ **Ambiguity and vagueness**
- 🚫 **Unethical or unsafe intent**

The framework aims to encourage safe, verifiable and responsible usage of generative AI systems.

## 📁 Project Structure

promptguard/
├── prompts/ # Prompt templates and patterns
├── evaluation/ # Evaluation logic and scoring metrics
├── tests/ # Unit tests (pytest)
├── notebooks/ # Main Jupyter Notebook demo
├── results/ # Visual output (plots, stats)
├── .env # API keys (not committed)
├── README.md # This file
├── requirements.txt # Project dependencies


## 🚀 Getting Started

### 🔗 Clone and install:
```bash
git clone https://github.com/valentinaschiavon99/promptguard
cd promptguard
python3 -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
🧪 Setup your OpenAI API key
Create a file .env in the root directory:

OPENAI_API_KEY=your-key-here
📊 Evaluation Strategy

PromptGuard is evaluated using:

✅ Formal correctness (format rules, regex)
🧠 Semantic consistency (embedding similarity)
📏 Rule compliance (content & structure validation)
Each metric is applied to a test set of 50 manually created prompt-output pairs. Results are visualized with Matplotlib.

🧪 Testing

Unit tests are written using pytest to ensure correctness of scoring functions and API logic:

pytest tests/
📓 Notebook Demo

The full execution and evaluation flow is documented in:

notebooks/promptguard_demo.ipynb
📜 License

MIT License – see LICENSE file for details.

✍️ Author

Valentina Schiavon
Bachelor in Wirtschaftsinformatik
AAU Klagenfurt
