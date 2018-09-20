#Hangman
#James O'Brien and Jack Antes

run = True

counter = 0
global counter2

guessed = []

word = input("Player 1, Enter a Word: ")
print("\n" * 50)

l = list(word)
mx = len(l)

def Fentress():
    returnword = ""
    for letter in word:
        if letter in guessed:
            returnword += letter
        else:
                returnword += " _ "
    print(returnword)
    if returnword == word:
        print('That is the word, my dude! good job!')
        counter2 = counter2 + 1
        
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
        print('you dead, boi. up to the pearly gates ya go. Bye bye now. Ba-bye!')
        run = False

    if counter2 == 1:
        run = False
