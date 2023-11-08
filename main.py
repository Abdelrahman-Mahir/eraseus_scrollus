from tkinter import *
from tkinter import ttk, messagebox
from prompts import PromptGenerator
import time


# Create the Prompt Generator
def get_prompt():
    prompt_gen = PromptGenerator()
    prompt = prompt_gen.get_prompt()
    print(prompt)
    typing_area.config(state="normal")
    typing_area.delete("1.0", END)
    typing_area.insert(END, prompt)
    typing_area.config(state="disabled")


# Dark Mode
def dark_mode():
    global is_dark
    if not is_dark:
        root.tk.call("set_theme", "dark")
        is_dark = True
    else:
        root.tk.call("set_theme", "light")
        is_dark = False


# Blinking Light
def blink_light(state):
    if state == "standby":
        blinking_light.config(image=empty_dot)
        root.update()
    elif state == "typing":
        blinking_light.config(image=green_dot)
        root.update()
    elif state == "warning":
        while True:
            blinking_light.config(image=red_dot)
            root.update()
            time.sleep(0.5)
            blinking_light.config(image=empty_dot)
            root.update()
            time.sleep(0.5)
    elif state == "stop":
        blinking_light.config(image=red_dot)
        root.update()


# Start App
def start_app():
    if goal_entry.get() == "":
        messagebox.showerror("Error", "Please Enter your goal for this session.")
    else:
        try:
            goal = int(goal_entry.get())
            if goal <= 0:
                messagebox.showerror("Error", "Please Enter a valid goal for this session.")
            else:
                blink_light("typing")
                start_btn.config(state="disabled")
                prompts_btn.config(state="disabled")
                goal_entry.config(state="disabled")
                typing_area.config(state="normal")
                typing_area.focus()
                blink_light("typing")
        except ValueError:
            messagebox.showerror("Error", "Please Enter a valid goal for this session.")


# Timer Starter
def timer_starter(event):
    if len(event.keysym) == 1:
        blink_light("typing")
        timer()


# Timer Function
def timer():
    global typing_time
    while typing_time < 5:
        typing_time += 1
        time.sleep(1)
        blink_light("typing")
    while 5 < typing_time < 10:
        typing_time += 1
        time.sleep(1)
        blink_light("warning")
    if typing_time > 10:
        refresh
# Create the root window
root = Tk()
root.title("Eraseus Scrollus")
root.geometry("1000x700")

# Set the initial theme
is_dark = False
root.tk.call("source", "azure.tcl")
root.tk.call("set_theme", "light")

# Dark Mode Button
theme_btn = ttk.Checkbutton(root, text='Dark Mode', style='Switch.TCheckbutton', command=dark_mode)
theme_btn.grid(row=0, column=0, padx=10, pady=10)

# Blinking light Images
green_dot = PhotoImage(file="green_dot.png")
red_dot = PhotoImage(file="red_dot.png")
empty_dot = PhotoImage(file="empty_dot.png")

# Create the frame
blinking_light = ttk.Label(root, image=empty_dot)
blinking_light.grid(row=0, column=1, padx=10, pady=10)

# Create the Buttons
prompts_btn = ttk.Button(root, text="Start with a Prompt", command=get_prompt)
prompts_btn.grid(row=1, column=0, padx=10, pady=10)
no_prompts_btn = ttk.Button(root, text="Start with No Prompt")
no_prompts_btn.grid(row=1, column=1, padx=10, pady=10)

# User Goal
goal_label = ttk.Label(root, text="Your Words Goal: ")
goal_label.grid(row=2, column=0, padx=10, pady=10)
goal_entry = ttk.Entry(root, width=20)
goal_entry.grid(row=2, column=1, padx=10, pady=10)

# Start Button
start_btn = ttk.Button(root, text="Start", command=start_app)
start_btn.grid(row=3, column=0, padx=10, pady=10, columnspan=2)

# Typing Area
typing_area = Text(root, width=100, wrap='word')
typing_area.grid(row=4, column=0, padx=10, pady=10, columnspan=2)
typing_area.config(font=("consolas", 12), undo=True, wrap='word', highlightthickness=1, borderwidth=3, border=1,
                   state="disabled")

# State Initialization
blink_light("standby")

# Variable Initialization
typing_time = 0
# Event Listeners
root.bind("KeyPress", timer_starter, add="+")
root.mainloop()
