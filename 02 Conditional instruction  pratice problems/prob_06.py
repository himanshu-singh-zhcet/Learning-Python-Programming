sentence = input("Enter a english sentence: ")

words = sentence.split()
print(words)
words.sort()
print(words)
newSentence = ""
for x in words:
    newSentence += x + " "
    
print(newSentence)