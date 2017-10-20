import os
import subprocess  


filestring="log.txt"
def A1():
	os.system("start " + filestring)
def A2():
	subprocess.Popen(filestring)  
def A3():
	os.startfile(filestring)
def A4():
	os.spawnv(filestring)

A1()