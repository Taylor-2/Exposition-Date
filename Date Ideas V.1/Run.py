from Tkinter import *
from random import *

window=Tk()
window.iconbitmap('heart.ico')
window.title("Date Ideas")
window.geometry("220x100")

def submit():
	vari=ideaEvar.get()
	if (vari != "") and (vari != " "):
		file=open("Idea List.txt","a")
		file.write(str(vari)+"\n")
		file.close()
		ideaEvar.set("")
	else:
		pass

def random():
	file=open("Idea List.txt","r")
	data=file.readlines()
	file.close()
	leng=len(data)
	number=randint(0,leng-1)
	randideafun=data[number]
	leng=len(randideafun)
	randideafun=str(randideafun[0:leng-1])
	print str(number) + " : " + str(randideafun)
	randidea.set(randideafun)

ideaEvar=StringVar()
ideaEvar.set("")
randidea=StringVar()
randidea.set("")

file=open("Idea List.txt","r")
data=file.readlines()
file.close()

ideaL=Label(window,text="Idea: ")
ideaE=Entry(window,textvariable=ideaEvar,width=20)
butt=Button(window,text="Submit",command=submit)
randL=Entry(window,text=randidea)
randButt=Button(window,text="Random",command=random)

ideaL.grid(column=0,row=0)
ideaE.grid(column=1,row=0)
butt.grid(row=2,column=0,padx=20)
randL.grid(row=1,columnspan=2)
randButt.grid(row=2,column=1)

window.mainloop()