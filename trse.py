#program to get number of words wrt each line in trse.txt
file=open("trse.txt","r")
for line in file.readlines():
	words=len(line.split())
	print words
	