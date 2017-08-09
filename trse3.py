#program to count and print the punctuation marks in trse.txt
f = open("trse.txt","r")
symbol = "!@#$%^&*()_-:;?/><,."
lines = f.readlines()
for i in lines:
	thisline = i.split()
	print thisline
	found=0
	for key in symbol:
		if symbol==found:
			found+=1
		print i.count(key),key		


