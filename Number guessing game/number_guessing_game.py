import random
num = random.randrange(1,10)
guess = int(input("Enter any number: "))
while num!= guess:
    if guess < num:
        print("the number is too low")
        guess = int(input("Please enter number again: "))
    elif guess > num:
        print("the number is too high!")
        guess = int(input("Please enter number again: "))
    else:
        break
print("Great, you guessed it right!!")
