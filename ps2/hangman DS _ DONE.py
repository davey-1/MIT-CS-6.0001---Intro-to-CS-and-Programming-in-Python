# Problem Set 2, hangman.py
# Name: David Sheu
# Collaborators:
# Time spent: 9.5 hrs total

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("------------")
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()



def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    
    
    s_w_list = list(secret_word)
    
    s_w_l_c = s_w_list[:]
        
    for i in s_w_l_c:
        if i in letters_guessed:
            s_w_list.remove(i)
            
    if len(s_w_list) == 0:
            return 1
        #If all letters have been guessed, returns true
        
    return 0
    
                


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
   
    # example: 
    # secret_word = 'apple'
    # letters_guessed = 'p', 'e'
    # get_guessed_word returns "_ pp _ e"

    
    guessed_word = [] 
    
    for char in secret_word:
        if char in letters_guessed:
            guessed_word.append(char)
        else: 
            guessed_word.append("_ ")
                
    return ''.join(guessed_word)
            


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''

    
    alphabet = string.ascii_lowercase
    
    alphabet_list = list(alphabet)
    
    
    for char in alphabet_list[:]:
        if char in list(letters_guessed): 
            alphabet_list.remove(char)
            
            

    return ''.join(alphabet_list)


    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
     
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
  
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.

    '''
    

    
    # Welcome message
    
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is",len(secret_word),"letters long.")
    print("------------")
    print("Hint: the word is:",secret_word) #feel free to remove when playing the game
 
    
    
    letters_guessed = []

    num_guesses = 6
    num_warnings = 3
    
    #NB: If a user picks a right letter twice, nothing changes.
    #    If a user picks a wrong letter twice, they get guesses removed.  I could change it but... I don't see much extra value in it.

    
    while num_guesses > 0 and num_warnings > 0:
        
        if is_word_guessed(secret_word,letters_guessed) == 1:
            break

        print("")
        print("You have",num_guesses,"guesses left.")
        print("Available letters:",get_available_letters(letters_guessed))
        letter_picked = input("Please guess an available letter: ")

        
        if letter_picked in get_available_letters([letters_guessed]):
            letters_guessed.append(letter_picked)
            if letter_picked in list(secret_word):
                print("Good guess:",get_guessed_word(secret_word,letters_guessed))
            else:
                num_guesses = num_guesses - 1
                print("Oops! The letter",letter_picked,"is not in the word:",get_guessed_word(secret_word,letters_guessed))
        else: 
            num_warnings = num_warnings - 1
            print (letter_picked,"is not a valid letter, You have",num_warnings,"warnings left:",get_guessed_word(secret_word,letters_guessed))



    #Game conclusion below, positive or negative
    total_score = num_guesses*len(secret_word)
    
    if is_word_guessed(secret_word,letters_guessed) == 1:
        print("Congrats! You've correctly guessed the word:",secret_word,"with",num_guesses,"tries left.")
        print("Your total score for this game is:",total_score)
    else:
        print("------------")
        print("Sorry, you ran out of guesses.  The word was",secret_word)
    
    print("------------")





# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = list(my_word)
    
    for i in my_word:
        if i == ' ':
            my_word.remove(' ')
        else: 
            pass
    
    if len(my_word) == len(other_word):
        for i in range(len(my_word)):
            my_char = my_word[i]
            other_char = other_word[i]
            if my_char == "_":
                pass
            elif my_char != other_char:
                return False
        return True
    return False
    
    


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             **Keep in mind** that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    
    
   
    
    print(">>>show_possible_matches"+"(\""+my_word+"\")")
    
    
    matches = []
        
    for other_word in wordlist:
        if match_with_gaps(my_word, other_word):
            matches.append(other_word)
        else: pass
    
    return ' '.join(matches)
    

        



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
 
    

    # Welcome message
    
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is",len(secret_word),"letters long.")
    print("------------")
    print("Hint: the word is:",secret_word) #feel free to remove when playing the game
 
    
    
    letters_guessed = []

    num_guesses = 6
    num_warnings = 3
    
    #NB: If a user picks a right letter twice, nothing changes.
    #    If a user picks a wrong letter twice, they get guesses removed.  I could change it but... I don't see much extra value in it.

    
    while num_guesses > 0 and num_warnings > 0:
        
        if is_word_guessed(secret_word,letters_guessed) == 1:
            break

        print("")
        print("You have",num_guesses,"guesses left.")
        print("Available letters:",get_available_letters(letters_guessed))
        letter_picked = input("Please guess an available letter: ")

        
        #added variable b/c it's called so often.
        guessed_word = get_guessed_word(secret_word, letters_guessed)
            
        
        if letter_picked in get_available_letters([letters_guessed]):
            letters_guessed.append(letter_picked)
            if letter_picked in list(secret_word):
                print("Good guess:", get_guessed_word(secret_word, letters_guessed))
                print("----------")
                
            else:
                num_guesses = num_guesses - 1
                print("Oops! The letter",letter_picked,"is not in the word:", guessed_word)
                print("----------")
        ### New code for hints starts here

        
        elif letter_picked == "*":
                print("Possible word matches are: ")
                print(show_possible_matches(guessed_word))
                print("----------")
                
        ### new code ends here

        else: 
            num_warnings = num_warnings - 1
            print (letter_picked,"is not a valid letter, You have",num_warnings,"warnings left:", guessed_word)
            print("----------")



    #Game conclusion below, positive or negative
    total_score = num_guesses*len(secret_word)
    
    if is_word_guessed(secret_word,letters_guessed) == 1:
        print("Congrats! You've correctly guessed the word:",secret_word,"with",num_guesses,"tries left.")
        print("Your total score for this game is:",total_score)
    else:
        print("------------")
        print("Sorry, you ran out of guesses.  The word was",secret_word)
    
    print("------------")





# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist) # "apple" if you want to test
   # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
