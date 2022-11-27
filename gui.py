from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,Scrollbar
from tkinter import scrolledtext
from tkinter import INSERT, WORD, END, DISABLED, RIGHT
import tkinter.scrolledtext as tkk
import time
is_on = True
import speech_recognition as sr
def takeCommandVoice():
	r = sr.Recognizer()
	query = "None"
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source, duration=1)
		r.dynamic_energy_threshold = True
		r.pause_threshold = 1
		audio = r.listen(source)
	try:
		query = r.recognize_google(audio, language='en-in')
	except Exception as e:
		print("[I am really sorry, Say that again please...]")
	return query

def switch():
	global is_on
	# Determine is on or off
	if is_on:
		button_1.config(image = stop)
		print("turned on")
		entry_1.config(state = "disabled")
		is_on = False
	else:
		button_1.config(image = listen)
		entry_1.config(state = "normal")
		is_on = True
		print("turned off")

def input(event):

	inp=entry_1.get() 
	if(inp=="voice"):
		
		text_area.insert(INSERT, takeCommandVoice())
	print("input registered")
	entry_1.delete(0, "end")
window = Tk()

window.geometry("850x650")
window.title("Roger Virtual Assistant")
window.configure(bg = "#FFFFFF")
window.iconbitmap("images/favicon (1).ico")

canvas = Canvas(
	window,
	bg = "#FFFFFF",
	height = 650,
	width = 850,
	bd = 0,
	highlightthickness = 0,
	relief = "ridge"
)

canvas.place(x = 0, y = 0)



listen = PhotoImage(file = "images/listen.png")
stop = PhotoImage(file = "images/stop.png")

button_1 = Button(
	image=listen,
	borderwidth=0,
	highlightthickness=0,
	command=switch,
	relief="flat",
	fg="#FFFFFF",
	bg="#FFFFFF",
	highlightbackground="#FFFFFF",
)
button_1.place(
	x=377.0,
	y=568.0,
	width=172.554931640625,
	height=69.0
)

entry_image_1 = PhotoImage(
	file="images/textbox.png")
entry_bg_1 = canvas.create_image(
	702.0,
	602.5,
	image=entry_image_1
)
entry_1 = Entry(
	bd=0,
	bg="#D9D9D9",
	fg="#000000",
	highlightthickness=0,
	disabledforeground="#D9D9D9",
	disabledbackground="#D9D9D9"
)
entry_1.place(
	x=595.5,
	y=568.0,
	width=213.0,
	height=67.0
)
entry_1.bind("<Return>", input)

image_image_1 = PhotoImage(
	file="images/image_1.png")
image_1 = canvas.create_image(
	184.0,
	368.0,
	image=image_image_1
)

text_area=tkk.ScrolledText(window,width=45,height=25,relief="flat",font=("Times New Roman",11),wrap=WORD,state=DISABLED)
text_area.grid(column=0,pady=37,padx=400)

window.resizable(False, False)
window.mainloop()





