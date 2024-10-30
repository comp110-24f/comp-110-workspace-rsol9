"""This program will have us guess a number and see if it is less than, greater than, equal to the secret number 7"""

__author__ = "730771611"


def guess_a_number() -> (
    None
):  # defining the function guess_a_number, itll ask the user user input and printstesting that guess_a_number has the correct output for a specific guess.

    secret: int = 7  # local variable secret
    guess: int = int(input("Guess a number: "))  # the input number the person guesses

    print(
        "Your guess was " + str(guess)
    )  # guess has to be a string to add!!! this will be printed

    if guess == secret:  # if the guess = secret, int version, itll print correct
        print("You got it!")
    elif guess > secret:  # if guess>secret, int version, itll print too high
        print("Your guess was too high! The secret number is " + str(secret))
    else:  # if guess<secret, int version, itll print too low
        print("Your guess was too low! The secret number is " + str(secret))

    return None


"""the entire block of code above is the print function"""
if __name__ == "__main__":  # calling the main function
    guess_a_number()
