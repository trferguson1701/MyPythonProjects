
#Modules
import random

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