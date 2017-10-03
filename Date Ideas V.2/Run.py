from tkinter import *
from random import *
'''

Mark, Lets just put our stuff and ideas, changes, etc. in this comment block, I'll run through all the code and 
comment it so you can better understand the tkinter stuff.

I'm not sure what you mean... what else do you want to filter the idea by?

And also, all comments tabbed over are explanations, and the ones in the actual body are placeholders

Also I created each of the price/effort text files
It would be cool if we could have all the supporting files in a folder in the Date Ideas V.2 folder
like ----> Date Ideas V.2
				Run.py
				Supporting folder
					Low
					Med
					High
					Free
					Icon
It's a shit file explanation, but you get my idea, I just don't know how to call them when they're like that

'''
window=Tk()
window.iconbitmap('heart.ico')			#Initializes the GUI, sets the icon, name, and window size
window.title("Date Ideas")
#window.geometry("250x100")

def submit():								#Function that runs every whenever you hit the submit button
	vari=ideaEvar.get()						#Goal is to get it to take the value of the idea field, and the price/effort field
	#filename=								#Then write the idea to the correct price text file
	if (vari != "") and (vari != " "):
		file=open("Idea List.txt","a")		#Currently only writes to the single "Idea List.txt" file
		file.write(str(vari)+"\n")
		file.close()
		ideaEvar.set("")
	else:
		pass

def random():										#Picks the first set of randomness, picks the number that determines what the
	randomone=randint(0,100)						#Price/effort will be
	if (randomone>=0 and randomone<=53):
		#final=function("Free.txt")					#Currently works but isn't fully set up, just need to attach the correct files to the statements
		print("free")
	elif (randomone>53 and randomone<=79):
		#final=function("Low.txt")
		print("low")						#These print statements are placeholders until we get the function(): hooked up
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

def function(filename):							#Function to take the price/effort filename from random(): then open the file, and choose an idea
	file=open(filename,"r")						#Second set of randomness
	data=file.readlines()		
	file.close()								#Currently works in theory, but hasn't been tested
	leng=len(data)
	number=randint(0,leng-1)
	chosen=data[number]							#Still accepting better names than the function function
	leng=len(chosen)
	chosen=str(chosen[0:leng-1])
	return chosen

def delete():									#Function that will eventually delete an idea on a buttonclick
	print ("Deeeeelete")						#Currently not set up, just a placeholder

def dates():
	pass 							#Lets make sure to put comments because I wanted to create a function
									#that takes the variable created from random() then continues filtering it

ideaEvar=StringVar()			#Initializes variables for the tkinter
ideaEvar.set("")
randidea=StringVar()
randidea.set("")
price=StringVar()
price.set("Price/Effort")

file=open("Idea List.txt","r")			#Grabs the date ideas from the file, might actually be unnessecary
data=file.readlines()
file.close()

menu=OptionMenu(window, price, "Free ($0)", "Low ($5-$10)", "Medium ($10-$25)", "High ($25+)")			#Price/effort drop down menu... not sure how to pull the selection
ideaL=Label(window,text="Idea: ")																		#idea label --> "Idea: " top left of the GUI
ideaE=Entry(window,textvariable=ideaEvar,width=20)														#Idea Entery field
butt=Button(window,text="Submit",command=submit)														#Submit Button
randE=Entry(window,text=randidea)																		#Random Entery field --> I want this to be a label in the final version, but im not sure why it dosent work, if you want to mess around with it just change the "Entery" after the variable to "Label"
randButt=Button(window,text="Random",command=random)													#Random Button
randL=Label(window,text="Random: ")																		#Random Label --> "Random: "    Unnessecary once we get the random entery field to be a label
delbutt=Button(window,text="Delete Idea",command=delete)												#Delete Button

ideaL.grid(column=0,row=1)									#Initializes each GUI element
ideaE.grid(column=1,row=1)									#Also sets the relative positions in the window
butt.grid(row=3,column=1)									
randE.grid(row=2,column=1)									#You can mess with the padding to get a better look with 
randButt.grid(row=3,column=0,padx=25)						#		pady=*Some number*      and     padx=*Some number*
randL.grid(row=2,column=0)
delbutt.grid(row=3,column=3)
menu.grid(row=1,column=2)


window.mainloop()							#Loops the GUI window, if the GUI isn't working, check that this is still here