import os

def function(ideaname, price):
	#Get ideaname
	#Get price
	#filename=formatprice(price)
	filename=price
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
		ctr += 1
	os.remove(filename + ".txt")
	file=open(filename + ".txt","a")
	leng=len(list1)
	ctr=0
	while(ctr<leng):
		file.write(list1[ctr])
		ctr += 1
	file.close()

ideaname = "h9"
price = "High"
function(ideaname,price)
