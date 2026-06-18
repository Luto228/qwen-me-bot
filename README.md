<img src="https://img.shields.io/badge/Made%20with-Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/Status-In%20Progress-blueviolet?style=for-the-badge" alt="Status">

# qwen-me-bot

This project is designed to become a universal Telegram bot that can read your messages, copy your communication style, and answer on your behalf while you are away.

## What it does

- Reads Telegram chat history from exported JSON files
- Cleans and extracts relevant message data
- Prepares your personal messaging style for AI-driven response modeling
- Aims to behave like your digital conversational twin

## Important setup step

To make the bot work, you must create a folder named `messages_for_ai` in the project root and place your exported Telegram chats inside it.

### How to export your Telegram chats

1. Open Telegram.
2. Open a chat.
3. Tap the three dots menu.
4. Choose `Export chat`.
5. Deselect all optional checkboxes.
6. Make sure to select `JSON` format.
7. Export and save the file into `messages_for_ai`.

## Required folder structure

The bot expects:

- `messages_for_ai/`
  - `your_chat_export.json`
  - `another_chat_export.json`

The script will scan the folder for `.json` files and extract messages automatically.

## How to run

Use Python to run the main script:

```bash
python main.py
```

The script will print how many messages it collected and show the first few cleaned entries.

## Notes

- The bot is intended to be a flexible Telegram assistant.
- It will read your exported chat history and use it to learn your messaging style.
- Right now the bot can only read your chats and remove all the noise, leaving only the cleaned messages in the terminal.
- More functionality will be added soon.
- The exported JSON files are mandatory for the bot to function.
