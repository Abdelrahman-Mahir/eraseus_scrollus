from tkinter import *
from tkinter import ttk, messagebox
from prompts import PromptGenerator
import time


# Create the Prompt Generator
def get_prompt():
    """Get a prompt from the Prompt Generator and display it in the typing area"""
    prompt_gen = PromptGenerator()
    prompt = prompt_gen.get_prompt()
    print(prompt)
    typing_area.config(state="normal")
    typing_area.delete("1.0", END)
    typing_area.insert(END, prompt)
    typing_area.config(state="disabled")


# Dark Mode
def theme_changer():
    """Change the theme of the app between light and dark"""
    global is_dark
    if not is_dark:
        root.tk.call("set_theme", "dark")
        is_dark = True
        theme_btn.config(text="Dark Theme")
    else:
        root.tk.call("set_theme", "light")
        is_dark = False
        theme_btn.config(text="Light Theme")


# Blinking Light
def blink_light(state):
    """Change the blinking light according to the state of the app, and to warn the user if they are not typing"""
    if state == "standby":
        blinking_light.config(image=empty_dot)
        root.update()
    elif state == "typing":
        blinking_light.config(image=green_dot)
        root.update()
    elif state == "warning":
        blinking_light.config(image=red_dot)
        root.update()
        root.after(500, blink_light, "standby")
    elif state == "stop":
        blinking_light.config(image=red_dot)
        print("This Stop Stage from blink_light")
        root.update()


# Start App
def start_app():
    """Start the app when the user clicks the start button. Check if the user has entered a valid goal.
    If not, show an error message."""
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
    """Start the timer when the user starts typing"""
    global typing_time
    if event.keysym and typing_area.cget("state") == "normal":
        typing_time = time.time()


# Timer Function
def timer():
    """Count the time since the last key press, and change the blinking light accordingly"""
    global typing_time
    current_time = time.time()
    if typing_time != 0:
        if current_time - typing_time < 5:
            blink_light("typing")
        elif 5 < current_time - typing_time < 10:
            blink_light("warning")
            print("This Warning Stage")
        elif 10 < current_time - typing_time < 15:
            blink_light("stop")
            print("This Stop Stage")
        elif current_time - typing_time > 15:
            refresh()
    # The following line is for debugging
    # print(f"Current Time: {current_time}\n Typing Time: {typing_time}\n Duration: {current_time - typing_time}")


# Update the timer and goal checker functions every second
def update_functions():
    """Update the timer and goal checker functions every 1 second"""
    timer()
    goal_checker()
    # Schedule the update every 1 second
    root.after(1000, update_functions)


# Goal Checker
def goal_checker():
    """Check if the user has reached the words' goal"""
    if typing_time != 0:
        goal = int(goal_entry.get())
        text = typing_area.get("1.0", END)
        words = text.split()
        if len(words) >= goal:
            save_btn.config(state="normal")
            print("Goal Reached")
        else:
            print("Goal Not Reached")


# Saving Progress
def saving_progress():
    text = typing_area.get("1.0", END)
    today = time.strftime("%d%m%Y")
    time_now = time.strftime("%H%M%S")
    with open(f"{today} {time_now}.txt", "w") as file:
        file.write(text)


# Refresh function
def refresh():
    """Refresh the app to the initial state"""
    global typing_time
    typing_time = 0
    goal_entry.config(state="normal")
    goal_entry.delete(0, END)
    typing_area.delete("1.0", END)
    typing_area.config(state="disabled")
    start_btn.config(state="normal")
    prompts_btn.config(state="normal")
    save_btn.config(state="disabled")
    blink_light("standby")
    messagebox.showinfo("Time's Up!", "You didn't type for more than 15 seconds. Try Again.")


# ---------------------------- UI SETUP ------------------------------- #
# Create the root window
root = Tk()
root.title("Eraseus Scrollus")
root.geometry("1000x700")

# Set the initial theme
is_dark = True
root.tk.call("source", "azure.tcl")
root.tk.call("set_theme", "dark")

# Dark Mode Button
theme_btn = ttk.Checkbutton(root, text='Dark Theme', style='Switch.TCheckbutton', command=theme_changer)
theme_btn.grid(row=0, column=0, padx=10, pady=10)

# Blinking light Images
green_dot = PhotoImage(file="green_dot.png")
red_dot = PhotoImage(file="red_dot.png")
empty_dot = PhotoImage(file="empty_dot.png")

# Creating the blinking light
blinking_light = ttk.Label(root, image=empty_dot)
blinking_light.grid(row=0, column=1, padx=10, pady=10)

# Create the Buttons
prompts_btn = ttk.Button(root, text="Start with a Prompt", command=get_prompt)
prompts_btn.grid(row=1, column=0, padx=10, pady=10)
save_btn = ttk.Button(root, text="Save Progress", state="disabled", command=saving_progress)
save_btn.grid(row=1, column=1, padx=10, pady=10)

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
typing_time = 0
root.after(0, update_functions)

# Event Listeners
root.bind("<KeyPress>", timer_starter)

root.mainloop()
