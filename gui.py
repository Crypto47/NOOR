from tkinter import *
import os
import openai

import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to
# speech
def SpeakText(command):
	
	# Initialize the engine
	engine = pyttsx3.init()
	engine.say(command)
	engine.runAndWait()
	
	
# Loop infinitely for user to
# speak

while(1):
	
	# Exception handling to handle
	# exceptions at the runtime
	try:
		
		# use the microphone as source for input.
		with sr.Microphone() as source2:
			
			# wait for a second to let the recognizer
			# adjust the energy threshold based on
			# the surrounding noise level
			r.adjust_for_ambient_noise(source2, duration=0.2)
			
			#listens for the user's input
			audio2 = r.listen(source2)
			
			# Using google to recognize audio
			MyText = r.recognize_google(audio2)
			MyText = MyText.lower()

			print("Did you say ",MyText)
			SpeakText(MyText)
			
	except sr.RequestError as e:
		print("Could not request results; {0}".format(e))
		
	except sr.UnknownValueError:
		print("unknown error occurred")

os.environ['OPENAI_API_KEY']='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'
openai.api_key = os.getenv("OPENAI_API_KEY")

# GUI
root = Tk()
root.title("N O O R")

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 15"
FONT_BOLD = "Helvetica 14 bold"

def liaqut(prompt):
    query = prompt

    response = openai.Completion.create(
                model="davinci:ft-personal-2022-12-24-13-38-53",
                prompt="The following is a conversation with a therapist and a user. The therapist is NOOR, who uses compassionate listening to have helpful and meaningful conversations with users. NOOR is empathic and friendly. NOOR's objective is to make the user feel better by feeling heard. With each response, NOOR offers follow-up questions and multiple choice questions to encourage openness and tries to continue the conversation in a natural way. \n\nNOOR-> Hello, I am your personal mental health assistant. What's on your mind today?\nUser->"+query+"NOOR->",
                temperature=0.89,
                max_tokens=162,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0.6,
                stop=["\n"]
    )
    respond=response['choices'][0]['text']
    return respond

# Send function
def send():
	send = "User -> " + e.get()
	answer=liaqut(e.get())
	txt.insert(END, "\n" + send)


	user = e.get().lower()

	txt.insert(END, "\n" + "NOOR -> " + answer)
	e.delete(0, END)


lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="N O O R  ChatBot", font=FONT_BOLD, pady=10, width=20, height=1).grid(
	row=0)

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=75)
txt.grid(row=1, column=0, columnspan=4)

scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)

e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=75)
e.grid(row=2, column=0)
# click_btn= PhotoImage(file='mic.png')

send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
			command=send).grid(row=2, column=1)
# mike = Button(root, image=click_btn, font=FONT_BOLD, bg=BG_GRAY,
# 			command=send).grid(row=2, column=2)

root.mainloop()
