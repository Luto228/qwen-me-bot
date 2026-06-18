import json
from second_step_clean_msg import second_step_clean_message

final_dialogues = second_step_clean_message()

print(f"😎 YES! WE COLLECT: {len(final_dialogues)} MESSAGES!")
print("\n👇 here are the first three\n" + "-" * 50)
for msg in final_dialogues[:3]:
    print(f"{msg['from_who']}: {msg['user_text']}\n" + "-" * 50)