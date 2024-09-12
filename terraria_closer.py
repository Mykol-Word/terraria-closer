import requests
import json
from datetime import datetime, timezone
import keyboard
import os

# Functions

def check_for_close_tag(close_tag, arm_time):
    headers = {
        'authorization': user_id
    }

    request = requests.get('https://discord.com/api/v9/channels/' + chat_id + '/messages', headers=headers)
    request_json = json.loads(request.text)
    if "message" in request_json:
        print("Get request failed. The response was '" + request.text + ".' This is likely due to invalid keys in 'keys.json'")
        exit(1)
    for message in request_json:
        message_time = datetime.fromisoformat(message['timestamp'])
        if(close_tag in message['content'] and message_time > arm_time):
            print("FOUND")
            return True
        
def get_keys():
    if not os.path.isfile('keys_template.json') and not os.path.isfile('keys.json'):
        print("No 'keys_template.json' or 'keys.json' file present. Program terminating")
        exit(1)
    if not os.path.isfile('keys.json') and os.path.isfile('keys_template.json'):
        os.rename('keys_template.json', 'keys.json')
    key_file = open('keys.json')
    key_json = json.load(key_file)
    key_file.close()

    return key_json['user_key'], key_json['chat_key']

# Main Program

user_id, chat_id = get_keys()

main_loop = 1

close_tag = input("Type your desired close tag:")

armed = input("Type 'ARM' to arm the server closer:")
while armed != "ARM":
    armed = input("Invalid input. Type 'ARM' to arm the server closer:")

arm_time = datetime.now(datetime.now().astimezone().tzinfo)
arm_time = arm_time.astimezone(timezone.utc)

print("Your close tag is '" + close_tag + "'")
print("Press 'q' to unarm the server closer")

while main_loop:
    if keyboard.is_pressed('q'):
        main_loop = 0

    if check_for_close_tag(close_tag, arm_time):
        main_loop = 0