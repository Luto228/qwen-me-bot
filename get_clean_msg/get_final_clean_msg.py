import os
import json
import time

import google.generativeai as genai

from config import GEMINI_API_KEY   

def get_final_clean_message(second_folder_path, third_folder_path):
    API_KEY = GEMINI_API_KEY
    SYSTEM_PROMPT = """
   You are a professional data engineer. Your task is to convert raw chat logs into the perfect JSON format for LLM training.
    You must accept a list of messages and return a STRICTLY valid JSON array, where:
    - Messages from regular people are assigned to the "user" role.
    - Messages from the author "Tom Prime" are assigned to the "assistant" role.

    CRITICAL FORMATTING RULES:
    1. DO NOT wrap the response in Markdown code blocks (NEVER use ```json or ```). 
    2. The response must start IMMEDIATELY with the opening square bracket '[' and end with the closing square bracket ']'.
    3. Output a single, continuous JSON array. NEVER create split arrays like ][ or ], [ inside the response.
    4. Do not include any pre-text, post-text, or explanations. Only the raw JSON string.

    Expected output format:
    [
        {"role": "user", "content": "friend's text"},
        {"role": "assistant", "content": "Tom's response"}
    ]
    """
    model = genai.GenerativeModel(
        model_name = "gemini-2.5-flash",
        system_instruction = SYSTEM_PROMPT
    )
    second_step_clean_msg = second_folder_path
    third_step_clean_msg = third_folder_path
    if not os.path.exists(second_step_clean_msg):
        return
    with open(second_step_clean_msg, "r", encoding = "utf-8") as f:
        data = json.load(f)
    for i in range(0, len(data), 400):
        time.sleep(2)
        batch = data[i: i + 400]
        prompt_content = json.dumps(batch, ensure_ascii = False)
        try:
            response = model.generate_content(prompt_content)

            with open(third_step_clean_msg, "a", encoding = "utf-8") as f:
                f.write(response.text + "\n")
        except Exception as e:
            print(f"Error! Exception: {e}")