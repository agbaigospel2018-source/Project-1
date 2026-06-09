name = input("Enter your Name: ").title()

match name:
    case "Harry" | "Hermione" | "Ron": #using the stroke symbol to assign the case to the different strings instead of weiting them on individual lines. You use the OR operator in case of if/elif/else
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who goes you? ")