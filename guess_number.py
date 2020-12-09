#Guess the number game

import random

print("Hello, what is your name?")
name =input()

l=1
h= 100
g = 14
number = random.randint(l,h)



print(name + ", can you guess my number? It's between "+str(l)+" and " + str(h))


for guesses in range(1,g):
    print("Guess:")
    guess = int(input())

    if guess < number:
        print("Your guess is too low")
    elif guess > number:
        print("Your guess is too high")
    else:
        
        break
        
if guess == number:
    print("Correct! You only needed " + str(guesses) + " guesses!")
else:
    print("Wrong! THe correct number was: " +str(number))



    

