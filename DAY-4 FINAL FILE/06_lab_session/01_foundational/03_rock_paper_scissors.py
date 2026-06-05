"""
    Final Project: Rock-Paper-Scissors

        1.) Ask user input for number of rounds (int)
            - If invalid input, keep asking until correct
        2.) For every round, do the following:
            2a.) Let user input "rock", "paper", or "scissors"
                - If invalid input, keep asking until correct
            2b.) Pick randomly from "rock", "paper", or "scissors"
            2c.) If user input beats random chocie, add score for user.
                 If random choice beats user, add score to CPU

        3.) Print winner and scores for both CPU and user
"""

import random

def get_valid_rounds() -> int:
    """
    Asks the user for the number of rounds to play.
    Keeps prompting until a valid integer input is provided.

    Returns:
        int: Number of rounds (positive integer)
    """
    # TODO: Implement input validation for number of rounds.
    pass

def get_user_choice() -> str:
    """
    Asks the user to input their choice of "rock", "paper", or "scissors".
    Keeps prompting until a valid input is provided.

    Returns:
        str: User's valid choice ("rock", "paper", or "scissors")
    """
    # TODO: Implement input validation for user choice.
    pass

def get_cpu_choice() -> str:
    """
    Randomly selects a choice for the CPU from "rock", "paper", or "scissors".

    Returns:
        str: CPU's randomly chosen move ("rock", "paper", or "scissors")
    """
    # TODO: Implement random choice selection for CPU.
    pass

def determine_winner(user_choice: str, cpu_choice: str) -> str:
    """
    Determines the winner of a round based on the user's and CPU's choices.

    Args:
        user_choice (str): User's choice ("rock", "paper", or "scissors")
        cpu_choice (str): CPU's choice ("rock", "paper", or "scissors")

    Returns:
        str: The winner ("user", "cpu", or "tie")
    """
    # TODO: Implement logic to determine the winner based on game rules.
    pass

def main() -> None:
    """
    Main function to run the Rock-Paper-Scissors game.
    It coordinates the game logic by calling other functions.
    """
    # TODO: Implement the flow of the game, including rounds, score tracking, and final result.
    pass

if __name__ == "__main__":
    main()
