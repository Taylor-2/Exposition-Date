from tkinter import *
from random import *

window=Tk()
window.iconbitmap('heart.ico')
window.title("Date Ideas")
#window.geometry("250x100")

def submit():
	vari=ideaEvar.get()
	#filename=
	if (vari != "") and (vari != " "):
		file=open("Idea List.txt","a")
		file.write(str(vari)+"\n")
		file.close()
		ideaEvar.set("")
	else:
		pass

def random():
	randomone=randint(0,100)
	if (randomone>=0 and randomone<=53):
		#final=function("Free.txt")
		print("free")
	elif (randomone>53 and randomone<=79):
		#final=function("Low.txt")
		print("low")
	elif (randomone>79 and randomone<=92):
		#final=function("Med.txt")
		print("med")
	elif (randomone>92 and randomone<=98):
		#final=function("High.txt")
		print("high")
	elif (randomone==99):
		print ("egg 1")
	elif (randomone==100):
		print ("egg 2")
	#print (final)
	#Whatever I need to put here so that it's displayed as a label

def function(filename):
	file=open(filename,"r")
	data=file.readlines()
	file.close()
	leng=len(data)
	number=randint(0,leng-1)
	chosen=data[number]
	leng=len(chosen)
	chosen=str(chosen[0:leng-1])
	return chosen

def delete():
	print ("Deeeeelete")

def dates():
	pass #Lets make sure to put comments because I wanted to create a function
	#that takes the variable created from random() then continues filtering it

ideaEvar=StringVar()
ideaEvar.set("")
randidea=StringVar()
randidea.set("")
price=StringVar()
price.set("Price/Effort")

file=open("Idea List.txt","r")
data=file.readlines()
file.close()

menu=OptionMenu(window, price, "Free ($0)", "Low ($5-$10)", "Medium ($10-$25)", "High ($25+)")
ideaL=Label(window,text="Idea: ")
ideaE=Entry(window,textvariable=ideaEvar,width=20)
butt=Button(window,text="Submit",command=submit)
randE=Entry(window,text=randidea)
randButt=Button(window,text="Random",command=random)
randL=Label(window,text="Random: ")
delbutt=Button(window,text="Delete Idea",command=delete)

ideaL.grid(column=0,row=1)
ideaE.grid(column=1,row=1)
butt.grid(row=3,column=1)
randE.grid(row=2,column=1)
randButt.grid(row=3,column=0,padx=25)
randL.grid(row=2,column=0)
delbutt.grid(row=3,column=3)
menu.grid(row=1,column=2)


window.mainloop()