import json
import os

def get_first_clean_messages(folser_path):
    for_ai_message = []
    FULL_PATH = folser_path

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
                    text_field = info_message.get("text")
                    collect_text = ""
                    if isinstance(text_field, str):
                        for_ai_message.append({
                            "user_id": info_message.get("id"),
                            "message_date": info_message.get("date"),
                            "from_who": info_message.get("from"),
                            "user_text": info_message.get("text"),
                            "reply_to_message_id": info_message.get("reply_to_message_id")
                        })
                    elif isinstance(text_field, list):
                        for j in text_field:
                            if isinstance(j, str):
                                collect_text += j
                            elif isinstance(j, dict):
                                collect_text += j.get("text", "")
                        for_ai_message.append({
                            "user_id": info_message.get("id"),
                            "message_date": info_message.get("date"),
                            "from_who": info_message.get("from"),
                            "user_text": collect_text,
                            "reply_to_message_id": info_message.get("reply_to_message_id")
                        })
    return for_ai_message