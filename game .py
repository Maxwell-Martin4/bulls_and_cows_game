import bulls_and_cows as bc

def main():
    # Please do not change this function!
    print('Welcome to Bulls and Cows death match!')
    again='y'
    while (again=='y'):
          play_game()
          again=input('would you like to play again? (y/n)')
    print('So long sucker!')


def play_game():
    ''' Plays a single interactive game of bulls and cows on the console'''
   

    #add your code here
    
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
