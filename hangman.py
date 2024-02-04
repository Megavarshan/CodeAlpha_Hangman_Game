import random
import string

WORDLIST_FILENAME = "C:/Users/Olek/6.00.1x/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    
    line = inFile.readline()
    
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True
            
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    
    secretList = []
    secretString = ''
    for letter in secretWord:
        secretList.append(letter)
    for letter in secretList:
        if letter not in lettersGuessed:
            letter = '_ '
        secretString += letter  
    return secretString
    
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    
    lowerCaseList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    remainingLetters = '' 
    for char in lettersGuessed:
        if char in lowerCaseList:
            lowerCaseList.remove(char)
    for letter in lowerCaseList:
        remainingLetters += letter + ' '
    return remainingLetters[:-1]

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
    
    lettersGuessed = []
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.'
    mistakesMade = 0
    while mistakesMade < 8:
        print '-----------'
        print 'You have ' + str(8 - mistakesMade) + ' guesses left.'
        print 'Available letters: ' + getAvailableLetters(lettersGuessed)
        userGuess = str(raw_input('Please guess a letter: '))
        userGuess = userGuess.lower()
        if userGuess not in lettersGuessed:
            lettersGuessed += userGuess
            
            if userGuess in secretWord:
                print 'Good guess: '  + getGuessedWord(secretWord, lettersGuessed)
            else:    
                print 'Oops! That letter is not in my word: '  + getGuessedWord(secretWord, lettersGuessed)
                mistakesMade += 1
            if isWordGuessed(secretWord, lettersGuessed):
                break
        else:
            print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed)
    print '-----------'
    if isWordGuessed(secretWord, lettersGuessed):
        print 'Congratulations, you won!'
    else:
        print 'Sorry, you ran out of guesses. The word was ' + secretWord
        

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
