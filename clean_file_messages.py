import json
import os

def get_clean_messages():
    for_ai_message = []
    FULL_PATH = "messages_for_ai"

    if os.path.exists(FULL_PATH):

        for file_name in os.listdir(FULL_PATH):

            if file_name.endswith(".json"):
                
                file_full_path = os.path.join(FULL_PATH, file_name)

                with open(file_full_path, "r", encoding = "utf-8") as f:
                    file_json = json.load(f)
                
                file_message = file_json.get("messages", [])
                
                for info_message in file_message:
                    if info_message == "broken" or not info_message.get("from"):
                        continue
                    if info_message.get("type") != "message" or not info_message.get("text"):
                        continue 
                    clean_message = {
                        "user_id": info_message.get("id"),
                        "message_date": info_message.get("date"),
                        "from_who": info_message.get("from"),
                        "user_text": info_message.get("text"),
                        "reply_to_message_id": info_message.get("reply_to_message_id")
                    }
                    for_ai_message.append(clean_message)
    return for_ai_message