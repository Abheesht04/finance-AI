Finance Engine V1

Requirements

1. Python 3.8.2 (not tested on versions beyond this)
2. Ollama
3. Qwen3:8B

install ollama at : https://ollama.com/download

commands to run-
ollama pull qwen3:8b
git clone https://github.com/yourusername/finance-AI.git
python -m venv .venv
for windows - .venv\Scripts\activate
for mac/linux - source .venv/bin/activate
pip install -r requirements.txt
uvicorn ui.server:app --reload
open http://127.0.0.1:8000

