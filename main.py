from tkinter import *
import math


DEEP_BLUE = '#131F3D'
GREEN = '#98ca3f'
ORANGE = '#FF9F00'
FONT = ("Intro", 70, 'bold')
MEDIUM_FONT = ("Intro", 18, 'normal')
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ----------- TIMER RESET

def reset_timer():
    window.after_cancel(timer)  # Stop the timer count
    start_button.itemconfig(state="active")
    canvas.itemconfig(timer_text, text='00:00')
    status_text.itemconfig(text="Tiempo de concentración:")
    check_text.itemconfig(text='')
    # check_marks
    global reps
    reps = 0

# ----------- TIMER MECHANISM

def start_timer():
    global reps
    reps += 1

    start_button.config(state="disabled")

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_dow(long_break_sec)
        status_text.config(text='Descanso largo')
    elif reps % 2 == 0:
        count_dow(short_break_sec)
        status_text.config(text='Descanso corto:')
    else:
        count_dow(work_sec)
        status_text.config(text='Tiempo de concentración:')

# ----------------- COUNTDOWN MECHANISM ---------

def count_dow(count=(WORK_MIN * 60)):
    global timer

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f'0{count_sec}'

    if count_min < 10:
        count_min = f'0{count_min}'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        timer = window.after(1000, count_dow, count - 1)
    else:
        start_timer()
        check_marks = ''
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            check_marks += '✅'
        check_text.config(text=check_marks)

# ----------- UI SETUP

# Create a Window
window = Tk()
window.title("Platzidoro")
window.config(bg=DEEP_BLUE)

# Displaying an image as background using canvas
canvas = Canvas(width=300, height=500, bg=DEEP_BLUE, highlightthickness=0)
# Importing Icon images to the project
play_icon = PhotoImage(file="./images/app-icons/play-small.png")
pause_icon = PhotoImage(file="./images/app-icons/pause-small.png")
stop_icon = PhotoImage(file="./images/app-icons/stop-small.png")
bg_image = PhotoImage(file="./images/platzidoro-bg.png")
tomato_image = PhotoImage(file="./images/tomate-175.png")


canvas.create_image(150, 250, image=bg_image)
check_text = canvas.create_text(150, 150, text='', fill=GREEN, font=FONT)
canvas.create_image(150, 275, image=tomato_image)
# start_button = Button(image=play_icon, command=start_timer)
# stop_button = Button(image=stop_icon, command=reset_timer)
timer_text = canvas.create_text(150, 150, text='00:00', fill=GREEN, font=FONT)
status_text = canvas.create_text(150, 100, text='Continúa estudiando...', fill=ORANGE, font=MEDIUM_FONT)
canvas.grid(column=0, row=0, columnspan=2)

# play = lambda: PlaySound('./soundtrack/zen-gong.wav', SND_FILENAME)
# button = Button(text='Play', command=play)


window.mainloop()