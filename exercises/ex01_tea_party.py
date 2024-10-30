"""This program should be able to take the number of guests to a tea party and tell me how many tea bags i'll need, how many treats, and the cost."""

__author__: str = "730771611"


def main_planner(guests: int) -> None:
    """this is the function that brings everything together- it will print all outputs, no returns"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print(
        "Treats: " + str(treats(guests))
    )  # i forgot the plus sign thats why it took forever to get....
    print(
        "Cost: $" + str(cost(tea_bags(guests), treats(guests)))
    )  # it has to be cost, not costs, also the tea bag and treats number are dependent on the function, thats y they are my arguments


def tea_bags(people: int) -> int:
    """this function includes the number of guests attending the party to figure out how many tea bags are needed"""
    return people * 2  # take the number of people and * by 2


def treats(people: int) -> int:
    """this function will tell us the number of treats needed"""
    return int(
        tea_bags(people=people) * 1.5
    )  # take the number of tea bags found by using the number of people and * by 1.5


def cost(tea_count: int, treat_count: int) -> float:
    """this will tell you the cost of the tea bangs and treats combined"""
    return (tea_count * 0.50) + (
        treat_count * 0.75
    )  # take the number of tea bangs and find the cost for it and add it to the cost of treats


if __name__ == "__main__":  # this will allow me to run the code as if i have input
    main_planner(guests=int(input("How many guests are attending your tea party?")))
