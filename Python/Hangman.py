#Hangman
#James O'Brien and Jack Antes

counter = 0

guessed = []

word = input("Player 1, Enter a Word: ")
print("\n" * 50)

l = list(word)
mx = len(l)

def Tesla():
    for letter in word:
        for letter in guessed:
            print(letter)
        else:
            print('_')

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


run = True

while run == True:
    
    if word == 'water':
        counter = 6
        Hangman()
        print('you dead boi. water is nasty.')
        break
    
    print('There are ' + str(mx) + ' letters')
    
    guess = input("Player 2, guess a letter: ")
    guessed.append(guess)
    
    if guess in l:
        Hangman()
        print('That is correct, my dude!')
        Tesla()
        
    else:
        counter = counter + 1
        Hangman()
        print('No, not that one! Dad?')
        Tesla()
        
    if counter > 5:
        print('you dead, boi. up to the pearly gates ya go. Bye bye now. Ba-bye!')
        run = False
    
