======================================================================Keylogger Project==========================================================================
Description:

This project is a Python-based Keylogger that tracks and logs keyboard activity. It is designed for educational purposes and aims to showcase how to capture user input and track events like keypresses, Ctrl+C (copy), and Ctrl+V (paste) actions. This project uses the pynput library to listen for keyboard events and pyperclip to capture clipboard data.

Features:

Keystroke Logging: Logs every key press, including letters, numbers, and special characters.
Copy & Paste Detection: Detects and logs Ctrl+C (copy) and Ctrl+V (paste) actions along with the clipboard contents.
File Logging: All keystrokes and actions are saved in a keylog.txt file for later review.
Ethical Hacking Tool: Demonstrates basic keylogging and clipboard tracking in Python.

Technologies Used:

Python: The programming language used for development.
pynput: A library that allows us to monitor and control input devices (keyboard, mouse).
pyperclip: A library for clipboard interaction, used to capture text copied to the clipboard.

Installation Instructions:
Prerequisites:
Python 3.x: This project requires Python 3.x to run. You can download it from the official Python website. - https://www.python.org/downloads/

Install the necessary libraries with the following commands:

Steps to Set Up:
Clone the Repository:

1.Clone the project to your local machine by running the following command in your terminal:-
2.git clone https://github.com/your-username/keylogger-project.git
3.cd keylogger-project
4.pip install pynput pyperclip
5.python keylogger.py

How It Works:

The program continuously listens for keyboard events using the pynput library.
Ctrl+C and Ctrl+V actions are detected:
Ctrl+C will log [COPY] in the keylog.txt file.
Ctrl+V will log [PASTE] along with the text that was copied to the clipboard.
Regular keypresses are logged as well, with each key press being recorded in sequence.
When you press the Esc key, the program stops and the listener is stopped.
