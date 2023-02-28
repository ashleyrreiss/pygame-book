import random

print('I will flip a coin 1000 times. Guess how many times it will come up heads. (Press enter to begin.)')
input()
guess = input("Make a guess. ")
flips = 0
heads = 0
while flips < 1000:
    if random.randint(0, 1) == 1:
        heads = heads + 1
    flips = flips + 1

    if flips == 900:
        print('900 flips and there have been ' + str(heads) + ' heads.')
    if flips == 100:
        print('At 100 tosses, heads has come up ' + str(heads) + ' times so far.')
    if flips == 500:
        print('Halfway done, and heads has come up ' + str(heads) + ' times.')

if int(guess) > int(heads):
    margin = int(guess) - int(heads)
elif int(heads) > int(guess):
    margin = int(heads) - int(guess)

print()
print('Out of 1000 coin tosses, heads came up ' + str(heads) + ' times!')
if int(margin) > 0:
    print('You guessed ' + str(guess) + '. You were off by ' + str(margin) + '.')
elif int(margin) == 0:
    print('Wow! You guessed exactly right.')
