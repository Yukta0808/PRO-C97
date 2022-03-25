import random
print("Number Guessing Game")
number = random.randint(1,9)
chances = 0
print("Pick a random number between 1 & 9")

chances < 5;

guess = int(input("Enter your guess!:"))

if guess == number:
    print("OH, PARTY PARTY YEAH! You guessed it right!")
    

elif guess < number:
    print("Hmmmm, your guess is a tad bit low, guess a number higher than ", guess)

else:
    print("Dyude, you are a little bit higher than the actual number, guess a number lower than", guess)

chances += 1

if not chances < 5:
    print("Aw man! I was rooting for you, btw, its ok to lose, you can always try again :D, the number was ", number)
