
#Modules
import random



# Computer Guess Function
def computerGuess (lowval, highval, randnum, count=0):
    if highval >= lowval:
        guess = lowval + (highval - lowval) // 2
        if guess == randnum:
            return count
        #If the guess is greater than the number
        elif guess > randnum:
            count = count + 1
            return computerGuess(lowval, guess-1, randnum, count)
        else:
            count = count + 1
            return computerGuess(guess + 1, highval, randnum, count)
    else:
        #Number not found
        return -1


# Random Number Generator
randnum = random.randint(1,101)


# Initialize Variables
count = 0
guess = -99

# Create loop
while (guess != randnum):
    # Obtain User's Guess
    guess = (int)(input("Enter a number between 1 and 100:"))

    # Decision Construct

    if guess < randnum:
            print ("Guess Higher.")
    elif guess > randnum:
            print ("Guess Lower.")
    else:
            print ("Correct Guess!")
            break
    count = count + 1
# End loop

print ("It took you " + str(count) + " tries to guess the number!")
print ("It took the computer " + str(computerGuess(0,100, randnum)) + " tries to guess the number!")