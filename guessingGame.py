import random 

def computerGuess(lowval, highval, randnum, count=0):
    if highval >= lowval:
        guess = lowval + (highval - lowval) // 2
        # If guess is in the middle, it is found!
        if guess == randnum:
            return count
        
        # If "guess" is greater than the number,
        # it must be found in the lower half of the set of numbers
        # between the lower value and the guess
        elif guess > randnum:
            count = count + 1
            print(guess)
            return computerGuess(lowval, guess-1,randnum,count)
        # The number must be in the upper set of numbers
        # between the guess and the higher value
        else:
            count = count + 1
            print(guess)
            return computerGuess(guess + 1, highval,randnum,count)
        
    else:
        # number not found
        return -1


# end of function

# Generate a random number between 1 and 100
# Want to generate random number ONCE
# want to guess multiple times
randnum = random.randint(1,101)

count = 0
guess = -99 # because random number cannot be negative
while (guess != randnum):
    # Get the user's guess
    guess = (int)(input("Enter your guess between 1 and 100:"))

    if guess < randnum:
        print("increase your guess")
    elif guess > randnum:
        print("lower your guess")
    else : 
        print("you guessed it!")
    count +=1
# end of while loop

print("You took " + str(count) + " steps to guess the number")
print("Computer took "+str(computerGuess(0,100,randnum)) + " steps!")