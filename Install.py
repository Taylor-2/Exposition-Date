import shutil
import os
from tkinter import *

root = Tk()
root.title("Installer")
def CreateDesktop():
	#shutil.copy2("Exposition Date Main\\Exposition Date.lnk","C:\\users\\"+os.getlogin()+"\\desktop")
	print("Shortcut")
def CopyFiles():
	shutil.copytree("Exposition Date Main",path.get()+"\\Exposition Date")
	if (state.get() == 1):
		CreateDesktop()
	if (state1.get() ==1):
		print("Execute")
		#execfile(path.get()+"\\Exposition Date\\dist\\Exposition Date.exe")
	root.quit()

state=IntVar()
state.set(1)
state1=IntVar()
state1.set(1)
path=StringVar()
path.set("C:\\Users\\"+os.getlogin()+"\\Documents")

installbutton=Button(root,text="Install",command=CopyFiles)
desktop=Checkbutton(root, text="Create Desktop Icon", variable=state)
launch=Checkbutton(root, text="Launch When Finished", variable=state1)
pathentry=Entry(root,textvariable=path,width=40)
label=Label(root,text="Install Path:")

label.pack()
pathentry.pack()
desktop.pack()
launch.pack()
installbutton.pack()

mainloop()