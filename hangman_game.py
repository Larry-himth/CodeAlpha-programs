import random # allows random word selection

# list of secret words
words = ['apple','orange','mango','berry','banana']

# randomly choose one word from the list
SecretWord = random.choice(words)

guessedLetters = [] #list stores the guessed letters 
incorrectGuesses = 0 #count for incorrect guesses
maxGuesses = 6 # max number of incorrect guesses
wordGuessed =False # tracks whether the word has been fully guessed

while(incorrectGuesses<maxGuesses and wordGuessed == False):
    
    # ask the player to enter a letter
    guess = input("Enter a letter of a random fruit: ")
    
    # validate input
    if len(guess) != 1:
        print("It should be a single letter")
    elif guess in guessedLetters: #checks if the letter is already guessed
        print("You already guessed this letter")
        continue
    else:
        guessedLetters.append(guess) #stores the valid guessed letter
    
    # check if the guessed letter is in the secret word
    if guess in SecretWord:
        print("Correct guess")
    else:
        print("Wrong guess")
        incorrectGuesses += 1
        
    # show guessed letters and underscores for the missing letters
    for x in SecretWord:
        if x in guessedLetters:
            print(x, end=" ")
        else:
            print("_", end=" ")
        
    print("Guesses left: ",(maxGuesses-incorrectGuesses)) #displays remaining guesses
    print() #blank line for bette readability
    
    wordGuessed = True
    # check if any letter in the secret word has not been guesses
    for x in SecretWord:
        if x not in guessedLetters:
            wordGuessed = False
            break
    
# show results
if wordGuessed == True:
    print("Congratulations!\n You won")
else:
    print("Game over!\n You lost")
    print("The word was: " +str(SecretWord))

