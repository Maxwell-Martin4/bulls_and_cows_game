# maxmartin4
Bulls and Cows game

import random

def generate_secret():
    ''' Generates a 4 digit number with no repeat digits''
    It converts the number to a string and returns it'''

    # list of potential digits
    possible_digits = "0123456789"    
    
    # sample ensures no repeated numbers
    secret = (random.sample(possible_digits,4))
    empty_string = ""
    secret = (empty_string.join(secret))

    return secret

def how_many_bulls(guess,answer):
    ''' Returns the number of bulls as an int that the guess earns when the
    secret number is answer. answer and guess should be strings'''
   
    bulls = 0 
    
    # setting if conditions with accumulator 
    # to count number of match between both list
    if guess[0] == answer[0]:
        bulls += 1
    if guess[1] == answer[1]:
        bulls += 1
    if guess[2] == answer[2]:
        bulls += 1
    if guess[3] == answer[3]:
        bulls += 1

    return bulls

def how_many_cows(guess,answer):
    ''' Returns the number of cows as an int that the guess earns when the
    secret number is answer. answer and guess should be strings'''
   

    #add your code here
    cows = 0 
    
    # setting mutiple if conditions 
    # is not in same position 
    # and exist in other list 
    
    if guess[0] != answer[0] and answer[0]in guess:
        cows += 1
    if guess[1] != answer[1] and answer[1]in guess:
        cows += 1
    if guess[2] != answer[2] and answer[2]in guess:
        cows += 1
    if guess[3] != answer[3] and answer[3]in guess:
        cows += 1

    return cows

    import bulls_and_cows as bc

def main():
    print('Welcome to Bulls and Cows death match!')
    again='y'
    while (again=='y'):
          play_game()
          again=input('would you like to play again? (y/n)')
    print('So long sucker!')

def play_game():
    ''' Plays a single interactive game of bulls and cows on the console'''
   
    #setting variables 
    count = 1   
    answer = "aaaa"
    
    # answer assigned before loop so it stays the same
    answer = bc.generate_secret()
    guess = "aaaa"

    # while loop keeps game going until guess == answer
    while guess != answer:
        print ("attempt", count)
      
        # guess in while loop as it updates each time
        guess = input("guess 4 digit number: ")
        bulls = bc.how_many_bulls(guess, answer)
        cows = bc.how_many_cows(guess, answer)
        
        # printing no of attempts if guess is correct
        # else add one to count and restart loop
        if guess == answer:
            print("you guess correctly at attempt", count)
        else:
            print(f"{bulls} bulls and {cows} cows")
            count += 1

#call the main function to run the game
main()

    
