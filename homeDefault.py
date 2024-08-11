import streamlit as st
import zipfile
import os
import pyautogui
import time
import re
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

def send_messages(messages, images_folder, phone_number, stop_flag):
    for sender, message, is_image in messages:
        if stop_flag():
            st.warning("Process stopped by user.")
            break
        if is_image:
            image_path = os.path.join(images_folder, message)
            if os.path.exists(image_path):
                pywhatkit.sendwhats_image(phone_number, image_path, f'{sender} sent an image: {message}')
                time.sleep(5)  # Wait time to ensure the image is sent
            else:
                print(f"Image {message} not found in {images_folder}")
        else:
            time.sleep(1)
            pyautogui.write(f'{sender}: {message}')
            time.sleep(1)
            pyautogui.press('enter')
            time.sleep(1)

# Streamlit app
st.title("WhatsApp Message Sender")

# File uploader
uploaded_file = st.file_uploader("Upload a ZIP file", type="zip")

# Input fields
phone_number = st.text_input("Enter the phone number (with country code)")
sender_name = st.text_input("Enter the sender's name")

# Stop button
stop = st.button("Stop")

# Flag to control the process
stop_flag = False

if stop:
    stop_flag = True

if uploaded_file and phone_number and sender_name and not stop_flag:
    # Create directories if they don't exist
    if not os.path.exists('images'):
        os.makedirs('images')

    # Save uploaded file
    with open("uploaded.zip", "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Decompress the ZIP file
    with zipfile.ZipFile("uploaded.zip", 'r') as zip_ref:
        zip_ref.extractall()

    # Move images to the images folder and save the .txt file as chat.txt
    for file_name in zip_ref.namelist():
        if file_name.endswith('.txt'):
            os.rename(file_name, 'chat.txt')
        elif file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
            os.rename(file_name, os.path.join('images', file_name))

    # Read and send messages
    lines = read_messages_from_file('chat.txt')
    messages = extract_messages(lines, sender_name)
    send_messages(messages, 'images', phone_number, lambda: stop_flag)

    if not stop_flag:
        st.success("Messages sent successfully!")