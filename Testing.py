import os
import subprocess  


filestring="C:\\Users\\Dexter Hubbard\\Documents\\GitHub\\Exposition-Date\\Exposition Date Main\\dist\\Exposition Date.exe"
def A1():
	os.system("start " + filestring)
def A2():
	subprocess.Popen(filestring)  
def A3():
	os.startfile(filestring)
def A4():
	os.spawnv(filestring)
def A5():
	os.execfile(filestring)
A5()