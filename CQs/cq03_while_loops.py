"""in this assignment, i will write a function called num_instances and be given two strings, phrase and search_char (a single character), and num_instances should return the count of occurrences of search_char in phrase """

__author__ = "730771611"


def num_instances(
    phrase: str, search_char: str
) -> (
    int
):  # defining num_instances, the function that will see how many times a character is found in a phrase
    index: int = (
        0  # this is the variable that helps us get through the code by comparing the position in the phrase
    )
    count: int = (
        0  # this is a variable defining the total number of times we see this character
    )
    while index < len(
        phrase
    ):  # while loop to repeat this if statement for every character in the phrase, checking to make sure the character count we are on still fits in the length of the message
        if (
            search_char == phrase[index]
        ):  # if the character of the index of the phrase we are on equals the character we are looking for
            count = (
                count + 1
            )  # if it does, we add it to the count, if not we move on and add to the index to go to the next character in the phrase
            index = index + 1
        else:
            index = index + 1  # add to the index count

    return count  # the return value should be the count, needs to be within the function too!!!
