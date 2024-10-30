"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730771611"


def input_word() -> str:
    "this function will ask for a 5 letter word as an input"
    word: str = input("Enter a 5-character word:")
    if len(word) == 5:
        print(word)
    else:
        print("Error: Word must contain 5 characters.")
        exit()
    return word


def input_letter() -> str:
    "this function will ask for a character as an input"
    letter: str = input("Enter a single character:")
    if len(letter) == 1:
        print(letter)
    else:
        print("Error: Character must be a single character.")
        exit()
    return letter


def contains_char(word: str, letter: str) -> None:
    "this function will see if the character is in the word, where, and how many times"
    index: int = 0
    count: int = 0
    print("Searching for " + str(letter) + " in " + str(word))
    while index <= int((len(word) - 1)):
        if letter == word[index]:
            print(
                str(letter) + " found at index " + str(index)
            )  # printing we found a letter in the word and where
            count = (
                count + 1
            )  # adding to the word count because we found another letter
            index = index + 1  # adding to the count to move on to the next index
        else:
            index = index + 1  # adding to the count to move on to the next index
    if count == 0:
        print("No instances of " + str(letter) + " found in " + str(word))
    elif count == 1:
        print(str(count) + " instance of " + str(letter) + " found in " + str(word))
    else:
        print(str(count) + " instances of " + str(letter) + " found in " + str(word))


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
