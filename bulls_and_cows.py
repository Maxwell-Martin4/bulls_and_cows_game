import random

def generate_secret():
    ''' Generates a 4 digit number with no repeat digits''
    It converts the number to a string and returns it'''

    # list of potential digits
    # sample ensures no repeated numbers
    possible_digits = "0123456789"    
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
   
    cows = 0 
    
    # setting mutiple if conditions 
    # is not in same position 
    # and exist in other lists 
    
    if guess[0] != answer[0] and answer[0]in guess:
        cows += 1
    if guess[1] != answer[1] and answer[1]in guess:
        cows += 1
    if guess[2] != answer[2] and answer[2]in guess:
        cows += 1
    if guess[3] != answer[3] and answer[3]in guess:
        cows += 1

    return cows
    
