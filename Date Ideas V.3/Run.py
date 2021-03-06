from tkinter import *
from random import *
import os
import tkinter.messagebox as msg
ideanamefordelete="start"
pricefordelete="start"

window=Tk()
window.iconbitmap('back/heart.ico')					#Initializes the GUI, sets the icon, name, and window size
window.title("Date Ideas")
#window.geometry("250x100")

def submit(event=None):									#Function that runs every whenever you hit the submit button
	idea=ideaEvar.get()
	filename=price.get()
	if (idea != "") and (idea != " "):
		if (filename == "Price/Effort"):
			msg.showinfo('Error', "Price/Effort can't be blank")
		filename=formatprice(filename)
		writer(filename,idea)
		ideaEvar.set("")
		price.set("Price/Effort")
	else:
		print("Blank")

def formatprice(price):
	if (price == "Free ($0)"):
		price="Free"
	elif (price == "Low ($5-$10)"):
		price="Low"
	elif (price == "Medium ($10-$25)"):
		price="Med"
	elif (price == "High ($25+)"):
		price="High"
	return price

def random(event=None):									#Picks the first set of randomness, picks the number that determines what the
	global ideanamefordelete
	global pricefordelete
	randomone=randint(0,1000)
	if (randomone>=0 and randomone<=600):		#60%
		filename="Free.txt"
		final=pickerpt2(filename)
	elif (randomone>600 and randomone<=850):		#25%
		filename="Low.txt"
		final=pickerpt2("Low.txt")
	elif (randomone>850 and randomone<=950):		#15%
		filename="Med.txt"
		final=pickerpt2("Med.txt")
	elif (randomone>950 and randomone<=998):	#4.8%
		filename="High.txt"
		final=pickerpt2("High.txt")
	elif (randomone==999):						#0.1%
		final="egg1"
	elif (randomone==1000):						#0.1%
		final="egg2"
	randL["text"]=str(final)
	ideanamefordelete = final
	pricefordelete = filename

def writer(filename,idea):
	file=open("back/" + filename + ".txt","a")
	file.write(idea + "\n")
	file.close()

def pickerpt2(filename):						#Function to take the price/effort filename from random(): then open the file, and choose an idea
	file=open("back/" +filename,"r")						#Second set of randomness
	data=file.readlines()		
	file.close()
	leng=len(data)
	number=randint(0,leng-1)
	chosen=data[number]
	leng=len(chosen)
	chosen=str(chosen[0:leng-1])
	return chosen

def delete(event=None):									#Works except for getting the idea and price, you can see a demonstration in the EXE folder
	filename=pricefordelete
	file=open("back/" +str(filename),"r")
	data=file.readlines()
	file.close()
	leng=len(data)
	list1=[]
	ctr=0
	while(ctr<leng):
		temp = data[ctr]
		temp = temp[0:-1]
		if (temp != ideanamefordelete):
			list1.append(temp + "\n")
		else:
			pass
		ctr += 1
	os.remove("back/" +filename)
	file=open("back/" +filename,"a")
	leng=len(list1)
	ctr=0
	while(ctr<leng):
		file.write(list1[ctr])
		ctr += 1
	file.close()
	randL["text"]=""
	print("File Deleted")

ideaEvar=StringVar()							#Initializes variables for the tkinter
ideaEvar.set("")
randidea=StringVar()
randidea.set("")
price=StringVar()
price.set("Price/Effort")

menu=OptionMenu(window, price, "Free ($0)", "Low ($5-$10)", "Medium ($10-$25)", "High ($25+)")			#Price/effort drop down menu... not sure how to pull the selection
ideaL=Label(window,text="Idea: ")																		#idea label --> "Idea: " top left of the GUI
ideaE=Entry(window,textvariable=ideaEvar,width=20)														#Idea Entery field
butt=Button(window,text="Submit",command=submit)														#Submit Button
ideaE.bind("<Return>", submit)
ideaE.bind("<Delete>", delete)
window.bind("<F5>", random)
randL=Label(window,text="")																				#Random Entery field --> I want this to be a label in the final version, but im not sure why it dosent work, if you want to mess around with it just change the "Entery" after the ideaable to "Label"
randButt=Button(window,text="Random",command=random)													#Random Button
delbutt=Button(window,text="Delete Idea",command=delete)												#Delete Button

ideaL.grid(column=0,row=1)						#Initializes each GUI element
ideaE.grid(column=1,row=1)						#Also sets the relative positions in the window
butt.grid(row=3,column=1,sticky=EW)				#You can mess with the padding to get a better look with 
randButt.grid(row=3,column=0,sticky=EW)			#	pady=*Some number*      and     padx=*Some number*
randL.grid(row=2,columnspan=3)
delbutt.grid(row=3,column=2,sticky=EW)
menu.grid(row=1,column=2)

window.mainloop()								#Loops the GUI window, if the GUI isn't working, check that this is still here