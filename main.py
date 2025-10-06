import time
import threading
import tkinter as tk
from datetime import datetime

# The time (in seconds) the screen remains locked
LOCK_DURATION = 20
# The interval (in seconds) between locks
INTERVAL = 20

start_time = datetime.now()

def lock():
    print("The screen has been locked!")
    screen = tk.Tk()
    screen.attributes("-fullscreen", True)
    screen.configure(bg="black")

    label = tk.Label(
        screen,
        text="Hello! Time to rest your eyes!\nLook at something 20 feet away for 20 seconds.",
        fg="white",
        bg="black",
        font=("Helvetica", 100, "normal")
    )
    label.pack(expand=True)

    screen.after(LOCK_DURATION * 1000, screen.destroy)
    screen.mainloop()
    print("The screen has been unlocked!")

def loop():
    while True:
        for sec in range(INTERVAL, 0, -1):
            elapsed = datetime.now() - start_time
            mins_elapsed = elapsed.seconds // 60
            print(
                f"Next lock in: {sec//60} min {sec%60} sec",
                end="\r"
                # This retunrs the cursor to the start of the line
            )
            time.sleep(1)
        lock()

if __name__ == "__main__":
    print(f"20-20-20 rule monitor started at {start_time.strftime('%H:%M:%S')}")
    # Using a daemon thread to ensure it exits when the main program does, and does not block exit
    t = threading.Thread(target=loop, daemon=True)
    t.start()
    while True:
        time.sleep(1)

