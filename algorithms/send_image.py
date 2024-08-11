import pyautogui
import time
import re
import os
import pywhatkit

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
                if "archivo adjunto" in message:
                    image_match = re.search(r'(IMG-\d+-WA\d+\.jpg)', message)
                    if image_match:
                        image_name = image_match.group(1)
                        messages.append((sender, image_name, True))
                else:
                    messages.append((sender, message, False))
    return messages

def send_messages(messages, images_folder, phone_number):
    for sender, message, is_image in messages:
        if is_image:
            image_path = os.path.join(images_folder, message)
            if os.path.exists(image_path):
                pywhatkit.sendwhats_image(phone_number, image_path, f'{sender} sent an image: {message}')
                time.sleep(5)  
            else:
                print(f"Image {message} not found in {images_folder}")
        else:
            time.sleep(1)
            
            pyautogui.write(f'{sender}: {message}')
            time.sleep(1)

            pyautogui.press('enter')
            time.sleep(1)

file_path = 'chat.txt'
images_folder = 'images/'
phone_number = '+5' 
lines = read_messages_from_file(file_path)
messages = extract_messages(lines, 'Renato')
send_messages(messages, images_folder, phone_number)