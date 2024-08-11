import pyautogui
import time
import re

def read_messages_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return lines

def extract_messages(lines, sender_filter):
    messages = []
    for line in lines:
        match = re.search(r' - (.*?): (.*)', line)
        if match:
            sender = match.group(1)
            message = match.group(2)
            if sender.lower() == sender_filter.lower():
                messages.appqueend((sender, message))
    return messages

def send_messages(messages):
    for sender, message in messages:
        pyautogui.typewrite(f'{sender}: {message}')
        pyautogui.press('enter')
        time.sleep(1)  

file_path = 'chat.txt'
sender_filter = 'Jocelyn'

lines = read_messages_from_file(file_path)
messages = extract_messages(lines, sender_filter)
send_messages(messages)