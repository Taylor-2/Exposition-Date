from tkinter import *
import tkinter.messagebox as msg
import os

root = Tk()

log = []
log.append("Initializing...\n")
textvar=StringVar()
textvar.set("")
labeltext=StringVar()
labeltext.set("Start")

def submit(event=None):
	log.append("\n" + str(textvar.get()) + "\n")
	labeltext.set(textvar.get())
	textvar.set("")

def exit(event=None):
	os.remove("log.txt")
	file=open("log.txt","w")
	ctr1 = 0
	while(ctr1<len(log)):
		file.write(log[ctr1])
		ctr1 += 1
	file.close()
	os.system("start log.txt")
	quit()

enteryfield=Entry(root,textvariable=textvar,width=20)
enteryfield.bind('<Return>', submit)
enteryfield.bind('<Alt Escape>', exit)
submitbutton = Button(root,text="Submit", command = submit)
exitbutton= Button(root,text="Exit",command=exit)
resultslabel=Label(root,textvariable=labeltext)

enteryfield.pack()
resultslabel.pack()
submitbutton.pack()
exitbutton.pack()

mainloop()