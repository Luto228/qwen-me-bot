import json
import os

from datetime import datetime
from get_clean_msg.get_first_clean_msg import get_first_clean_messages

def second_step_clean_message(output_file_name):
    old_clean = get_first_clean_messages("messages_for_ai")

    second_step_clean_msg = "clean_msg/second_step_clean_msg.json"
    clean_message = []
    MAX_INTERVAL = 20

    current_user = None
    current_user_text = None
    current_user_data = None

    for j in old_clean:
        if current_user == None or current_user_text == None or current_user_data == None:
            current_user = j.get("from_who")
            current_user_text = j.get("user_text")
            current_user_data = j.get("message_date")
        else: 
            last_time = datetime.fromisoformat(current_user_data)
            current_time = datetime.fromisoformat(j.get("message_date"))
            time_difference = current_time - last_time
            time_difference = time_difference.total_seconds()
            if current_user == j.get("from_who") and time_difference <= MAX_INTERVAL:
                    current_user_text += " " + j.get("user_text", " ")
                    current_user_data = j.get("message_date")
            else:
                clean_message.append({
                    "from_who": current_user,
                    "user_text": current_user_text
                })
                current_user = j.get("from_who")
                current_user_text = j.get("user_text")
                current_user_data = j.get("message_date")
    with open(second_step_clean_msg, "w", encoding = "utf-8") as f:
        json.dump(clean_message, f, ensure_ascii= False, indent= 2)

    return clean_message