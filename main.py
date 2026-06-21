import os
import json
import google.generativeai as genai
from config import GEMINI_API_KEY

from get_clean_msg.get_second_clean_msg import second_step_clean_message
from get_clean_msg.get_final_clean_msg import get_final_clean_message

os.makedirs("clean_msg", exist_ok=True)

genai.configure(api_key=GEMINI_API_KEY)

SECOND_STEP_FILE = "clean_msg/second_step_clean_msg.json"
THIRD_STEP_FILE = "clean_msg/third_step_clean_msg.json"

print("🚀 Starting compilation and cleaning of all chats...")
final_dialogues = second_step_clean_message(SECOND_STEP_FILE)

print(f"\n😎 YES! WE COLLECTED: {len(final_dialogues)} MESSAGES TOTAL!")
print(f"📦 All messages are successfully saved to: {SECOND_STEP_FILE}")
print("\n👇 Here are the first three messages from the combined dataset:\n" + "-" * 50)

for msg in final_dialogues[:3]:
    print(f"{msg['from_who']}: {msg['user_text']}\n" + "-" * 50)

print("\n" + "=" * 50 + "\n")

print("🧠 Starting dataset labeling via Gemini API...")
print("⏳ This will take some time, as batches are being sent with a 2-second delay...")

get_final_clean_message(SECOND_STEP_FILE, THIRD_STEP_FILE)

print("\n" + "=" * 50 + "\n")
print(f"🔥 ALL DONE! The final dataset for Qwen training is saved to: {THIRD_STEP_FILE} 🔥")