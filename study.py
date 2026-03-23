import time

def start_study_session(minutes):
    seconds = minutes * 60
    print(f"Starting your {minutes} minute UNT study session... Go Mean Green! 🦅")
    
    # Simple countdown logic
    time.sleep(1) # This makes the program wait
    print("Time is up! Take a break.")

# Calling the function
session_length = 25  # You can change this number
start_study_session(session_length)
