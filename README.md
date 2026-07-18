Overview

This application is an AI-driven agent designed to automate the processing, data extraction, and analysis of invoices using a local Qwen model.
Important Notices

    Model Requirements: The Qwen model (approximately 10GB) is not included in this repository. You must install Ollama and download the model locally before executing the application.

    Configuration: Review all internal configuration files and path variables after cloning the repository. Ensure all directory paths are updated to match your local system environment to prevent file-loading errors or system directory collisions.

Prerequisites

Ensure the following software is installed on your system before proceeding:

    Python: Version 3.8.2. or any python version that supports below libraries.

    Ollama: Required to orchestrate and host the local LLM environment.

Installation
1. Configure the AI Model

You may install Ollama using either the graphical installer or the command-line interface.
Option A: Graphical Installer (Recommended for Windows/macOS)

    Visit the official Ollama download page.

    Download the installer for your operating system.

    Run the installer and follow the on-screen prompts to complete the setup.

Option B: Command Line (Linux/macOS)

For Linux and macOS users, you can install Ollama directly via your terminal:
Bash

curl -fsSL https://ollama.com/install.sh | sh

Fetch the Core Model

Once installed, verify the installation and fetch the core architecture model by running the following command in your terminal or command prompt:
Bash

ollama pull qwen3:8b

2. Clone the Repository

Clone the project repository to your local machine and navigate into the directory:
Bash

git clone https://github.com/finance-AI
cd finance-AI

3. Initialize the Virtual Environment

Create and activate a virtual environment to isolate project dependencies:
Bash

python -m venv .venv

Activation Commands:

    Windows (Command Prompt / PowerShell):
    Bash

    .venv\Scripts\activate

    macOS / Linux:
    Bash

    source .venv/bin/activate

4. Install Dependencies

Update your environment with the Python libraries defined in the requirements file:
Bash

pip install -r requirements.txt

Execution

Launch the local server interface using the following command:
Bash

uvicorn ui.server:app --reload

Once the terminal server processes initialize successfully, access the application dashboard via your web browser at:

http://127.0.0.1:8000
