#Odgadywanie liczby przy pomocy metody bisekcji
import math

print 'Please think of a number between 0 and 100!\n'

foot = 0
head = 100
goodGuess = ''

while (goodGuess != "c"):
    guess = math.floor((head + foot) / 2)
    print "Is your secret number {}?".format(int(guess))
    goodGuess = raw_input(
        "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if (goodGuess == "h"):
        head = guess
    elif (goodGuess == "l"):
        foot = guess
    elif (goodGuess != "c"):
        print "Sorry, I did not understand your input."

