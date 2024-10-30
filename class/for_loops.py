"""for loop practice"""

pets: list[str] = ["Louie", "Bo", "Bear"]
for animal in pets:
    print("Good boy, " + animal + "!")  # print(f"Good boy, {animal}!")


names: list[str] = ["Alyssa", "Janet", "Vrinda"]
for idx in range(0, len(names)):
    print(str(idx) + ": " + names[idx])
