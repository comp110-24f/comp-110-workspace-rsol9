"""a function that puts two strings together"""

__author__ = "730771611"


def concat(string1: str, string2: str) -> str:  # defining concat function
    print(string1 + string2)  # putting both together


word1: str = "happy"
word2: str = "tuesday"
"""defining both global variables"""
print(concat(word1, word2))

if __name__ == "__main__":
    print(concat(word1, word2))
