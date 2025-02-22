def get_integer_input() -> int:
    """
    This function prompts the user to enter an integer and returns the integer.
    It ensures the input is valid by catching any ValueErrors if the user enters non-integer data.
    """
    while True:
        try:
            # Prompting the user to input an integer
            user_input = input("Enter an integer: ")
            # Converting input to integer
            number = int(user_input)
            return number
        except ValueError:
            # Handling invalid input (non-integer)
            print("Invalid input. Please enter a valid integer.")

def check_even_odd(number: int) -> str:
    """
    This function checks if a number is even or odd.
    It uses the modulo operator (%) to determine divisibility by 2.
    
    Args:
    - number: The integer to check
    
    Returns:
    - A string message indicating whether the number is "Even" or "Odd"
    """
    if number % 2 == 0:
        return f"{number} is an Even number."
    else:
        return f"{number} is an Odd number."

def main():
    """
    Main program function that handles the flow of the program.
    It gets user input and checks if the number is even or odd.
    """
    number = get_integer_input()  # Get an integer from the user
    result = check_even_odd(number)  # Check if the number is even or odd
    print(result)  # Print the result

if __name__ == "__main__":
    main()
