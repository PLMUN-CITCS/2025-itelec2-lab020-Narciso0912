def get_integer_input() -> int:
    """
    Handles user input to obtain an integer.
    Returns:
        int: The integer entered by the user.
    """
    while True:
        try:
            number = int(input("Enter an integer: ").strip())
            return number
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def check_even_odd(number: int) -> str:
    """
    Determines if a given number is even or odd.
    Args:
        number (int): The integer to check.
    Returns:
        str: A formatted string indicating if the number is even or odd.
    """
    if number % 2 == 0:
        return f"{number} is an Even number."
    return f"{number} is an Odd number."

def main() -> None:
    """
    Main function to execute the even/odd checker program.
    """
    user_number = get_integer_input()
    result = check_even_odd(user_number)
    print(result)

if __name__ == "__main__":
    main()
