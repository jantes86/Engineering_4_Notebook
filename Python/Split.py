#M. Night Shyamalan's Split
#Jamsp A'Broon and Jark Hackspleen

x = input("Enter a sentence:")

words = x.split()

num = len(words)

for word in words:
    l = list(word)
    print(*l, sep= '\n')
    print('-')
