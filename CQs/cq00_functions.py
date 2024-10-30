""" __author__ = "730771611" """


def mimic(message: str) -> str:
    """this function will repeat back to you what you imput"""
    return message


def main() -> None:
    """this function won't return anything, but will be important to call the other functions you use"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
