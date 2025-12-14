import random

words = ['apple','orange','mango','berry','banana']
SecretWord = random.choice(words)

guessedLetters = []
incorrectGuesses = 0
maxGuesses = 6
wordGuessed =False

while(incorrectGuesses<maxGuesses and wordGuessed == False):
    
    guess = input("Enter a letter of a random fruit: ")
    
    if len(guess) != 1:
        print("It should be a single letter")
    elif guess in guessedLetters:
        print("You already guessed this letter")
        continue
    else:
        guessedLetters.append(guess)
    
    if guess in SecretWord:
        print("Correct guess")
    else:
        print("Wrong guess")
        incorrectGuesses += 1
        
    for x in SecretWord:
        if x in guessedLetters:
            print(x, end=" ")
        else:
            print("_", end=" ")
        
    print("Guesses left: ",(maxGuesses-incorrectGuesses))
    print()
    
    wordGuessed = True
    for x in SecretWord:
        if x not in guessedLetters:
            wordGuessed = False
            break
    
if wordGuessed == True:
    print("Congratulations!\n You won")
else:
    print("Game over!\n You lost")
    print("The word was: " +str(SecretWord))

