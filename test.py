from tkinter import *
from tkinter import ttk
from speedtest import Speedtest
import threading
from tkinter import ttk

# Create an instance of ttk.Progressbar
window = Tk()  # Define the "window" variable
progress_bar = ttk.Progressbar(window, mode='indeterminate')

# Function to update text labels with speed information
def update_text():
    progress_bar['value'] = 0  # Reset progress bar
    progress_bar.start(10)  # Start the progress bar animation
    t = threading.Thread(target=run_speed_test)
    t.start()

down_label = Label(window)  # Define the "down_label" variable
up_label = Label(window)  # Define the "up_label" variable

def run_speed_test():
    speed_test = Speedtest()
    download = speed_test.download()
    upload = speed_test.upload()
    download_speed = round(download / (10**6), 2)
    upload_speed = round(upload / (10**6), 2)
    down_label.config(text="Download Speed: " + str(download_speed) + " Mbps")
    up_label.config(text="Upload Speed: " + str(upload_speed) + " Mbps")
    progress_bar.stop()  # Stop the progress bar animation

# Function to clear the speed test results
def clear_results():
    down_label.config(text="")
    up_label.config(text="")

# GUI creation
window = Tk()
window.title("Internet Speed Testing")
window.geometry('420x250+250+150')

button_frame = Frame(window)
button_frame.pack(pady=20)

button = Button(button_frame, text="Check Speed", width=15, command=update_text, background='#49A')
button.grid(row=0, column=0, padx=5)

clear_button = Button(button_frame, text="Clear Results", width=15, command=clear_results, background='#49A')
clear_button.grid(row=0, column=1, padx=5)

progress_bar = ttk.Progressbar(window, orient=HORIZONTAL, length=300, mode='determinate')
progress_bar.pack(pady=10)

down_label = Label(window, text="", font=("Helvetica", 14))
down_label.pack()

up_label = Label(window, text="", font=("Helvetica", 14))
up_label.pack()

# Run GUI
window.mainloop()
