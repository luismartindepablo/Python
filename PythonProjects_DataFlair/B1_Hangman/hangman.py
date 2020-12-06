from os import system, name #to clear the console 
import random #to select word
import time #to pause execution

#define clear terminal function
def clear(): 
  
    # for windows 
    if name == "nt": 
        _ = system("cls") 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system("clear && printf '\e[3J'") #clear and reset scroll-back

clear()

#Playable words
words_to_guess = ["january","border","image","film","promise","kids","lungs","doll","rhyme","damage","plants"]

#global variables
word = None
word_answer = None
length = None
display = None
count = None
already_guessed = None

# Initial Steps to invite in the game:
print("Welcome to Hangman Game by Luis.\n")
name = input("Enter your name: ")
clear()

print("Hello " + name + "! Best of Luck!")
time.sleep(1) #pauses the execution during (sec)
print("The game is about to start!")
time.sleep(1)
print("Let's play Hangman!")
time.sleep(2)
clear()

#We define the main function that initializes the arguments
def main():

    global word
    global word_answer
    global length
    global display
    global count
    global already_guessed

    word = random.choice(words_to_guess) #randomly selects one element from the sequence
    word_answer = word #This will be unmutable
    length = len(word)
    display = '_' * length
    count = 0 #attempts
    already_guessed = []


# A loop to re-execute the game when the first round ends:
def play_loop():

    play_game = input("Do You want to play again?\ny = yes, n = no \n")

    while play_game not in ["y", "n", "Y", "N"]:
        play_game = input("Do You want to play again?\ny = yes, n = no \n")

    if play_game in ["y", "Y"]: #restart the game
        clear()
        main() #restart parameters
        hangman() #gameLoop

    elif play_game in ["n", "N"]: #interrupt the game
        clear()
        print("Thanks For Playing! We expect you back again!") 
        time.sleep(2)
        clear()
        exit()

# Initializing all the conditions required for the game:
def hangman():

    global word
    global display
    global count
    global already_guessed

    limit = 5
    guess = input("This is the Hangman Word: " + display + "\nEnter your guess: ")
    guess = guess.strip() #Deletes out spaces
    clear()

    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or not guess.strip().isalpha():
        print("Invalid input, Try a letter.\n")
        hangman()

    elif guess in already_guessed:
        print("Already checked. Try another letter.\n")
    
    elif guess.lower() in word: #check if correct letter
        already_guessed.extend([guess.upper(), guess.lower()])

        for ii in range(word.count(guess.lower())): #change all letters matched
            index = word.find(guess.lower())
            word = word[:index] + "_" + word[index + 1:] #delete letter from word
            display = display[:index] + guess.lower() + display[index + 1:] #add letter to display

        if word != "_" * length:
            print("Well done, " + guess.lower() + " was in the Word.")

    else:
        already_guessed.extend([guess.upper(), guess.lower()])
        count += 1

        if count == 1:
            
            print("Wrong guess. " + str(limit - count) + " guesses remaining.\n")

            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__    \n")

        elif count == 2:
            
            print("Wrong guess. " + str(limit - count) + " guesses remaining.\n")

            print("   _____ \n"
                  "  |/    |\n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__    \n")

        elif count == 3:
           
           print("Wrong guess. " + str(limit - count) + " guesses remaining.\n")

           print("   _____ \n"
                 "  |/    |\n"
                 "  |     |\n"
                 "  |     O\n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__    \n")

        elif count == 4:
            
            print("Wrong guess. " + str(limit - count) + " guesses remaining.\n")

            print("   _____   \n"
                  "  |/    |  \n"
                  "  |     |  \n"
                  "  |     O  \n"
                  "  |    /|\ \n"
                  "  |        \n"
                  "  |        \n"
                  "__|__      \n")

        elif count == 5:
            
            print("Wrong guess. You are hanged!!!")
            print("The word was: " + word_answer + ".")

            print("   _____   \n"
                  "  |/    |  \n"
                  "  |     |  \n"
                  "  |     |  \n"
                  "  |     O  \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__      \n") 

    if word == '_' * length:
        print("Congrats! The word was: " + word_answer + ".\nYou have guessed the word correctly!")
        play_loop() #restart

    elif count != limit:
        hangman()

    else:
        play_loop() #restart

#Main Game
main() #initialize
hangman() #play