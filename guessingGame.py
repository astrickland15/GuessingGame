import random

guess_count=0
rnd_num=random.choice(range(1,11))

def main():

    global guess_count
    num_guess=int(input("Guess a number between 1 and 10: "))
    
    

    if num_guess < rnd_num:
        print("You guessed too low, try again")
        guess_count += 1
        main()

    elif num_guess > rnd_num:
        print("You guessed too high, try again")
        guess_count += 1
        main()

    else:
         print("You guessed correctly!")
         guess_count +=1
         print("You took %d guesses. " % (guess_count))



            

    
        

if __name__ == "__main__":
     main()
    
  

    
    


    
    
    
    
    
 
   
    

if __name__ == "__main__":
     main()