from clean_file_messages import get_clean_messages
messages = get_clean_messages()
print(f"😎 YES! WE COLLECT: {len(messages)} MESSAGES!")
import pprint

if messages:
    print("\n👇 here are the first three")
    print("-" * 50)
    
    for msg in messages[0:3]:
        pprint.pprint(msg)
        print("-" * 50) 