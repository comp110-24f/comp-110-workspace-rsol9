"""The next step in our journey to implementing Wordle is to create a program that allows the player to make six guesses at your program’s secret word and provides an emoji representation of the accuracy of each guess, just like in the real game."""

__author__ = "730771611"


def input_guess(
    secret_word_len: int,
) -> (
    str
):  # this function will ask the user for a guessed word and see if it matches the length of the secret word

    guess: str = input(
        f"Enter a {secret_word_len} character word: "
    )  # define the variable guess as whatever the inputted word was

    while len(guess) != secret_word_len:
        print(f"That wasn't {secret_word_len} chars! ")
        guess: str = input(
            "Try again: "
        )  # have them reinput it if not --> using a variable in a string

    if len(guess) == secret_word_len:
        print(guess)

    return guess


def contains_char(
    secret_word: str, char_guess: str
) -> (
    bool
):  # this function is meant to see if a single character is present in the entire word(this character will be taken from the final guessed word's index that we are currently on)

    assert (
        len(char_guess) == 1
    )  # make sure the character is acc 1, which it will be bc it is the index of the guessed word we are on

    index: int = 0  # start count w 0

    while index < len(
        secret_word
    ):  # bc the while will keep running, make sure the index length is less that the length of the secret word the user will input
        if (
            secret_word[index] == char_guess
        ):  # although for now the user will input a character, this character will be taken from a later function, here just see if that character is the character at the index of the secret word
            return True  # if it is, return true because it is a bool
        index += 1

    return False


def emojified(
    guessed_word: str, secret_word: str
) -> (
    str
):  # this function will add emoji's to the contains_char function and take two parameters: the guessedword and the secretword

    assert len(guessed_word) == len(
        secret_word
    )  # make sure both parameters are the same length, if it's not don't do anything abt it

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    index: int = 0
    result: str = ""

    while index < len(
        guessed_word
    ):  # make sure the index is less than the length of the guess word bc that is what we are checking

        if (
            guessed_word[index] == secret_word[index]
        ):  # at this particular index, check if the index values of both words are the same
            result += GREEN_BOX

        elif contains_char(
            secret_word, guessed_word[index]
        ):  # if they arent, but present in the word
            "use the contains_char function --> this is what checks the entire word to see if it present in the word, it will run each time for each index placement, only 1 box can be present for each index value anyways so if it is false it will move on and if not, it will run the function knowing that that index will print true"
            result += YELLOW_BOX

        else:  # if neither of above were true
            result += WHITE_BOX

        index += (
            1  # now we can move on from this index bc the appropriate box has printed
        )
    return result


def main(
    secret: str,
) -> (
    None
):  # main function that runs the code, it'll do the print of the turns and boxes

    current_turn: int = 0  # variable to keep track of how many turns have been made

    won: bool = (
        False  # just in case the person guesses the word, include this function so the program ends
    )

    while (
        current_turn < 6 and not won
    ):  # as long as they have turns remaining AND they haven't won with their first guess keep the program going into the while loop... if they get it on their first try, skip below
        current_turn += 1  # add to the turn number bc they just inputted a word

        print(
            f"=== Turn {current_turn}/6 ==="
        )  # print the icon line of code that says what place you are at

        guessed_word: str = input_guess(
            len(secret)
        )  # the variable that takes the guessed word, use the function to make sure both are the same length

        emoji_result: str = emojified(
            guessed_word, secret
        )  # once the input_guess function has confirmed they are the same length, run it through emojified function -> it will give each index value in the guessed word an appropriate box in relation to the OG secret word, that entire collection of emoji's is in this variable

        print(emoji_result)  # print the collection of boxes

        if (
            guessed_word == secret
        ):  # in by this point the word is right this will confirm it --> this while loop will no longer run and move on, able to print that they won and in how many tries
            won = True

    if won:
        print(f"You won in {current_turn}/6 turns!")

    else:
        print(f"X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
