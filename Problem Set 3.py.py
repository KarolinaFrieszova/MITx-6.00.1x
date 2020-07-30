# Hangman game

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()
secretWord = chooseWord(wordlist).lower()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for i in secretWord:
        if i not in lettersGuessed:
            return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    word=''
    for i in secretWord:
        if i in lettersGuessed:
            word=word+i
        else:
            word=word+'_ '
    return word 


import string

alpha = string.ascii_lowercase
alphabet = list(alpha)
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''

    for i in lettersGuessed:
        if i in alphabet:
            alphabet.remove(i)
        else:
            pass
    return ''.join(alphabet)
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''

    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is', len(secretWord), 'letters long.')
    guesses = 8
    lettersGuessed = []
    
    while not isWordGuessed(secretWord, lettersGuessed) and guesses > 0:
        print("\n-----------") 
        print('You have', guesses, 'guesses left.')
        print('Available letters:', getAvailableLetters(lettersGuessed))
        guess = input('Please guess a letter: ').lower()
                
        if guess in secretWord:
            if guess in lettersGuessed:
                print('Oops! You\'ve already guessed that letter:', getGuessedWord(secretWord, lettersGuessed))
            else:
                lettersGuessed.append(guess)
                print('Good guess:', getGuessedWord(secretWord, lettersGuessed))
        else:
            print('Oops! That letter is not in my word:', getGuessedWord(secretWord, lettersGuessed))
            guesses -= 1
            
    if secretWord == guess:
        outcome = 'Congratulations, you won!'
    else:
        outcome = 'Sorry, you ran out of guesses. The word was else.'
    return outcome

secretWord = chooseWord(wordlist).lower()
print(hangman(secretWord))

