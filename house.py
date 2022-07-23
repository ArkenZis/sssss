from unittest import case


name = input("What's your name? ")

match name.title():
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")

    case "Draco":
        print("Slytherin")

    case _:
        print("Who?")
