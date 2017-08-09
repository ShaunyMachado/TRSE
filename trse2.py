#program to count and print the top 10 ocuuring words in trse.txt
words = file("trse.txt", "r").read().split() 
N=10
uniqueWords = sorted(set(words))[:N] 
for word in uniqueWords:
    print words.count(word), word



