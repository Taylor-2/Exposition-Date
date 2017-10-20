from tkinter import *
import os

root = Tk()

log = []
ctr = 0
log.append("Initializing...\n")
textvar=StringVar()
textvar.set("")
widthvar=20
whatev=StringVar()
whatev.set("Start")


def submit():
	global widthvar
	global whatev
	widthvar=int(textvar.get())
	log.append("\nVariable set to " + str(widthvar) + "\n")
	whatev.set(textvar.get())
	textvar.set("")
	log.append("textvar reset to null\n")

def exit():
	os.remove("log.txt")
	print("writing")
	file=open("log.txt","w")
	ctr1 = 0
	while(ctr1<len(log)):
		file.write(log[ctr1])
		ctr1 += 1
	file.close()
	os.system("start log.txt")
	quit()

ent=Entry(root,textvariable=textvar,width=widthvar)
submit = Button(root,text="Submit", command = submit)
whatever= Button(root,text="Exit",command=exit)
lab=Label(root,textvariable=whatev)

ent.pack()
lab.pack()
submit.pack()
whatever.pack()

mainloop()