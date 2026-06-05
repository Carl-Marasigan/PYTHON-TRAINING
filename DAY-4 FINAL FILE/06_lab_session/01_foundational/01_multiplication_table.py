"""
    Final Project: Multiplication Table Generator

        1.) Ask user input for the number to generate the multiplication table for (int)
            - If invalid input, keep asking until correct
        2.) Generate and display the multiplication table for that number (from 1 to 10)
            - Example: For number 5, the table will display:
              5 x 1 = 5
              5 x 2 = 10
              ...
              5 x 10 = 50

        3.) Print the multiplication table to the screen
"""

def get_valid_number() -> int:
    """
    Asks the user for a valid number to generate the multiplication table.
    Keeps prompting until a valid integer input is provided.

    Returns:
        int: The number for the multiplication table (positive integer)
    """
    # TODO: Implement input validation for the number.
    pass

def generate_multiplication_table(number: int) -> None:
    """
    Generates and prints the multiplication table for the given number.

    Args:
        number (int): The number for which the multiplication table will be generated.
    """
    # TODO: Implement the logic to generate and print the multiplication table.
    pass

def main() -> None:
    """
    Main function to run the Multiplication Table Generator.
    It coordinates the user input and prints the multiplication table.
    """
    # TODO: Implement the flow of the program, including input collection and table generation.
    pass

if __name__ == "__main__":
    main()


def get_valid_number() -> int:
    """
    Asks the user for a valid number to generate the multiplication table.
    Keeps prompting until a valid integer input is provided.

    Returns:
        int: The number for the multiplication table (positive integer)
    """
    while True:
        try:
            # Ask the user for input and convert it to an integer
            number = int(input("Enter a number to generate its multiplication table: "))
            return number
        except ValueError:
            # This catches cases where the user types letters or symbols instead of numbers
            print("Invalid input. Please enter a valid integer.")

def generate_multiplication_table(number: int) -> None:
    """
    Generates and prints the multiplication table for the given number.

    Args:
        number (int): The number for which the multiplication table will be generated.
    """
    print(f"\nMultiplication Table for {number}:")
    print("-" * 30)

    # Loop from 1 to 10 to generate the table
    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")

    print("-" * 30)

def main() -> None:
    """
    Main function to run the Multiplication Table Generator.
    It coordinates the user input and prints the multiplication table.
    """
    print("=== Multiplication Table Generator ===")

    # 1. Get a valid number from the user
    user_number = get_valid_number()

    # 2. Generate and display the table
    generate_multiplication_table(user_number)

if __name__ == "__main__":
    main()


    def get_valid_number() -> int:
        """
        Asks the user for a valid number to generate the multiplication table.
        Keeps prompting until a valid integer input is provided.

        Returns:
            int: The number for the multiplication table (positive integer)
        """
        while True:
            try:
                # Ask the user for input and convert it to an integer
                number = int(input("Enter a number to generate its multiplication table: "))
                return number
            except ValueError:
                # This catches cases where the user types letters or symbols instead of numbers
                print("Invalid input. Please enter a valid integer.")


    def generate_multiplication_table(number: int) -> None:
        """
        Generates and prints the multiplication table for the given number.

        Args:
            number (int): The number for which the multiplication table will be generated.
        """
        print(f"\nMultiplication Table for {number}:")
        print("-" * 30)

        # Loop from 1 to 10 to generate the table
        for i in range(1, 11):
            result = number * i
            print(f"{number} x {i} = {result}")

        print("-" * 30)


    def main() -> None:
        """
        Main function to run the Multiplication Table Generator.
        It coordinates the user input and prints the multiplication table.
        """
        print("=== Multiplication Table Generator ===")

        # 1. Get a valid number from the user
        user_number = get_valid_number()

        # 2. Generate and display the table
        generate_multiplication_table(user_number)


    if __name__ == "__main__":
        main()


