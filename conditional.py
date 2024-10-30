"""practicing my conditionals"""

def get_weather_report() -> str:
    """what to do when the weather gets bad"""
    weather: str = input("what is the weather?")
    if weather = "rainy" or weather =="cold":
        print("bring a jacket!")
    elif weather == "hot!":
        print("keep cool out there!")
    else:
        print("i don't recognize this weather.")
    return weather


def less_than_10(num: int) -> None:
    """tell us if num < 10"""
    dub: int = num * 2  # 14
    dub = dub - 1  # 13
    print(dub)
    if num < 10:
        print("Small number!")
    else:
        print("Big number!")
    print("Have a nice day!")


less_than_10(num=7)


def wake_up(alarm: bool) -> str:
    """return a message based on if the alarm is going off"""
    if alarm is True:
        return "Wake up! Go to Comp 110!"
    else:
        return "Keep sleeping, lol"


print(wake_up(alarm=False))


def check_first_letter(word: str, letter: str) -> str:
    """if the first character of a word is letter, it should return match!"""
    if letter == word[0]:
        return "match!"
    else:
        return "no match!"


print(check_first_letter(word="happy", letter="h"))
print(check_first_letter(word="happy", letter="s"))


def number_info(num: int) -> None:
    if num < 10:
        print("small number!")
    else:
        if num % 2 == 0:
            print("even number!")
        else:
            print(odd number!"")
    return num

number_info(num=11)
print(number_info(num=4)) 



def get_ticket_price() -> int:
    age: int = int(input("What is your age?"))
    if age <= 12:
        price: int = 5
    else:
        price: int = 10
    return price

    def get_ticket_price() -> int:
    age: int = int(input("What is your age?"))
    if age <= 12:
        price: int = 5
    elif age > 60:
        price: int = 5
    else:
        price: int = 10
    return price

    def get_ticket_price() -> int:
    age: int = int(input("What is your age?"))
    if (age <= 12) or (age > 60):
        price: int = 5
    else:
        price: int = 10
    return price

    def get_ticket_price() -> int:
    age: int = int(input("What is your age?"))
    if age <= 12:
        price: int = 5
    elif age <= 60:
        price: int = 10
    return price


def characters(msg: str) -> None:
    index: int=0
    while index < len(msg):
        print(msg(index))
        index = index + 1

characters(msg="You're 20??? It's okaay babygurl nobudies gotta konoww")