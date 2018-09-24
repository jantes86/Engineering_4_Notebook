#Hangman
#James O'Brien and Jack Antes

run = True

counter = 0

returnword = ""

guessed = []

word = input("Player 1, Enter a Word: ")
print("\n" * 50)

l = list(word)
mx = len(l)

def Fentress():
    global returnword
    returnword = ""
    for letter in word:
        if letter in guessed:
            returnword += letter
        else:
            returnword += " _ "
    print(returnword)
        
def Hangman():
    print("\n" * 50)
    if counter == 0:
        print('___')
        print('   | ')
        print(' ')
        print(' ')
        print(' ')
    if counter == 1:
        print('___')
        print('   | ')
        print('   o ')
        print(' ')
        print(' ')
    if counter == 2:
        print('___')
        print('   | ')
        print('   o ')
        print('  /')
        print(' ')
    if counter == 3:
        print('___')
        print('   | ')
        print('   o ')
        print('  /|')
        print(' ')
    if counter == 4:
        print('___')
        print('   | ')
        print('   o ')
        print('  /|\ ')
        print(' ')
    if counter == 5:
        print('___')
        print('   | ')
        print('   o ')
        print('  /|\ ')
        print('  /')
    if counter == 6:
        print('___')
        print('   | ')
        print('   o ')
        print('  /|\ ')
        print('  / \ ')

Hangman()

print('There are ' + str(mx) + ' letters.')  

while run == True:
    
    if word == 'water':
        counter = 6
        Hangman()
        print('you dead boi. water is nasty.')
        break
  
    guess = input("Player 2, guess a letter: ")
    guessed.append(guess)
    
    if guess in word:
        Hangman()
        print('That is correct, my dude!')
        Fentress()
        
    else:
        counter = counter + 1
        Hangman()
        print('No, not that one! Dad?')
        Fentress()
        
    if counter > 5:
        print('you dead, boi. You were here for a good time not a long time. The correct word was:  ' + word)
        run = False

    if returnword == word:
        print("You did it! I'm deaf, so I might not have heard your word correctly, but you did it!")
        break
