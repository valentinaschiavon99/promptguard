🔐 PromptGuard – LLM Prompt Risk Analyzer

PromptGuard is a practical project developed for the course
Neuere Methoden in der Computerlinguistik (510.607, 25S)
at Alpen-Adria-Universität Klagenfurt by Valentina Schiavon.

This tool analyzes prompts submitted to Large Language Models (LLMs) such as GPT-4 to detect and score security risks like prompt injection, ambiguous instructions, or unethical intent. The goal is to promote safe and responsible use of generative AI.

📂 Project Structure

data/ – test prompts and evaluation sets
src/ – modular code for analysis, scoring and feedback
notebook/ – Jupyter Notebook with all steps and results
🚀 Get Started

Clone the repository and install requirements:
```bash
git clone https://github.com/valentinaschiavon99/promptguard
cd promptguard
pip install -r requirements.txt
```

📊 Evaluation Strategy

PromptGuard uses both quantitative (accuracy, false positives) and qualitative (feedback clarity, user eval) metrics to assess prompt safety.

📜 License

MIT License – see LICENSE file for details.
