import os

ideaname="start"
price="start1"

def adjust():
	global ideaname
	ideaname = "h9"
	global price
	price = "High"

def function():
	adjust()

	filename=price
	print (filename)
	print (ideaname)

	file=open(filename + ".txt","r")
	data=file.readlines()
	file.close()
	leng=len(data)
	list1=[]
	ctr=0

	while(ctr<leng):
		temp = data[ctr]
		temp = temp[0:-1]
		if (temp != ideaname):
			list1.append(temp + "\n")
		else:
			pass
		ctr += 1
	os.remove(filename + ".txt")
	file=open(filename + ".txt","a")
	leng=len(list1)
	ctr=0
	while(ctr<leng):
		file.write(list1[ctr])
		ctr += 1
	file.close()

function()