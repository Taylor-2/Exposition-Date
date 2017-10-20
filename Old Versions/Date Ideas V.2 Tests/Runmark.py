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
		randnum = 0
		return randnum
	elif (randomone>53 and randomone<=79):
		#final=function("Low.txt")
		randnum = 1
		return randnum
	elif (randomone>79 and randomone<=92):
		#final=function("Med.txt")
		randnum = 2
		return randnum
	elif (randomone>92 and randomone<=98):
		#final=function("High.txt")
		randnum = 3
		return randnum
	elif (randomone==99):
		randnum = 4
		return randnum
	elif (randomone==100):
		randnum = 5
		return randnum
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

def dates(randnum): #this function I think should be used for actually
#selecting the dates. it takes the value created in random() then it
#filters it down to even further results. If we could attach this to
#take files the the text file then we are set.
	if randnum == 0:
		print ("free")
		return "a"
	elif randnum == 1:
		print("low")
		return "b"
	elif randnum == 2:
		print("med")
		return "c"
	elif randnum == 3:
		print("high")
		return "d"
	elif randnum == 4:
		print("egg 1")
		return "e"
	elif randnum == 5:
		print("egg 2")
		return "f"
	 #Lets make sure to put comments because I wanted to create a function
	#that takes the variable created from random() then continues filtering it
	
def mash(): #I'm unsure if this was necessary, just made a function
#that calls both dates() and random() to be used then display the
#output
	testy = random()
	testy1 = dates(testy)
	print(testy1)
	randE["text"] = "The Random Idea is: " + str(testy1)
	return testy1

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
randE=Label(window,text= 'The Random Idea is: ')
randButt=Button(window,text="Random",command=mash)
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