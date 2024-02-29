def calculator():
    while True:
        try:
            first_number = float(input("Please provide a number: "))
            break
        except:
            print("Invalid input. Please try again.")

    while True:
        function = input("Please choose an operator (+, -, /, *): ")
        if function in ["+", "-", "/", "*"]:
            break
        else:
            print("Invalid input. Please try again.")

    while True:
        try:
            second_number = float(input("Please provide a number: "))
            break
        except:
            print("Invalid input. Please try again.")

    if function == "+":
        result = first_number + second_number
    elif function == "-":
        result = first_number - second_number
    elif function == "/":
        result = first_number / second_number
    elif function == "*":
        result = first_number * second_number
    else:
        result = "Invalid operator"

    print("Your result is: ", result)
    print()


if __name__ == "__main__":
    while True:
        calculator()

        if input("Do you want to go again? ").lower() not in ["y", "yes"]:
            break

        print()

    print("Thanks for using my Python Calculator :)")