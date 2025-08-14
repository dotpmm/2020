import time
import threading
import tkinter as tk
from datetime import datetime

LOCK_DURATION = 20
INTERVAL = 1200

start_time = datetime.now()

def lock():
    print("LOCKED")
    screen = tk.Tk()
    screen.attributes("-fullscreen", True)
    screen.configure(bg="black")

    label = tk.Label(
        screen,
        text="2020",
        fg="white",
        bg="black",
        font=("Helvetica", 120, "bold")
    )
    label.pack(expand=True)

    screen.after(LOCK_DURATION * 1000, screen.destroy)
    screen.mainloop()
    print("UNLOCKED")

def loop():
    while True:
        for sec in range(INTERVAL, 0, -1):
            elapsed = datetime.now() - start_time
            mins_elapsed = elapsed.seconds // 60
            print(
                f"Next lock in: {sec//60} min {sec%60} sec",
                end="\r"
            )
            time.sleep(1)
        lock()

if __name__ == "__main__":
    print(f"20-20-20 rule monitor started at {start_time.strftime('%H:%M:%S')}")
    t = threading.Thread(target=loop, daemon=True)
    t.start()
    while True:
        time.sleep(1)

