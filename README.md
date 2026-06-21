<img src="https://img.shields.io/badge/Made%20with-Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"> <img src="https://img.shields.io/badge/Status-Ready%20for%20context-blue?style=for-the-badge" alt="Status">

# qwen-me-bot

This project is ready for content generation: all data preparation is complete and all processing steps are fully operational.

## What this project does

- Collects exported Telegram chats from the `messages_for_ai` folder.
- Cleans and merges messages, removing unnecessary noise (system notifications, logs, etc.).
- Prepares and structures content for the Gemini API.
- Saves intermediate results to `clean_msg/second_step_clean_msg.json`.
- Automatically formats and outputs the final training-ready dataset to `clean_msg/third_step_clean_msg.json`.

## Important setup steps before running

1. Create a folder named `messages_for_ai` in the project root.
2. Export your Telegram chats in **JSON format** and place the exported files into the `messages_for_ai` folder.
3. Open `config.py.example`, copy it, rename the copy to `config.py`, and replace `YOUR_GEMINI_TOKEN` with your actual Gemini API key.

> ⚠️ **Important:** Never commit your `config.py` with real tokens to GitHub! Make sure it is added to your `.gitignore`.

## Expected folder structure

- `config.py` (created from `config.py.example`)
- `requirements.txt`
- `messages_for_ai/`
  - `chat1.json`
  - `chat2.json`
- `clean_msg/`
  - `second_step_clean_msg.json`
  - `third_step_clean_msg.json`

## Installation and Run

### 🛠️ On Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python main.py
```
### 🍎 On Linux / macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py
```
For subsequent runs on Linux/macOS, remember to activate the environment first using source .venv/bin/activate.

### How it works
# The execution flows through three main phases:

- **Extraction**: The script reads all JSON files in messages_for_ai and extracts text messages.

- **Merging**: Consecutive messages from the same author are merged to maintain conversation flow.

- **Refactoring** : The structured data is passed to the Gemini API in optimized batches to format it into a flawless dataset for training LLMs (like Qwen).

### Limitations and Notes
- Messages are processed by the Gemini API in batches.

- Thanks to our bulletproof pipeline, the output is saved as a structured dataset, but it is always recommended to verify clean_msg/third_step_clean_msg.json using your IDE's built-in JSON syntax validation.

### Next Updates
- **🤖 Phase 2 (Upcoming)**: A dedicated, standalone Telegram bot powered by aiogram 3.x that acts as your AI clone in direct messages (DMs).

- **👥 Phase 3**: Integration into group chats and userbot capabilities to allow the clone to converse on your behalf in real-time.