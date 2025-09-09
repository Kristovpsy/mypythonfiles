# List of valid moves in the game
moves: list[str] = ["rock", "paper", "scissors"]

# Display available moves with numbers
for i, move in enumerate(moves, start=1):
    print(f"{i}. {move}")

print()  # Empty line for better readability
choice = input("Select a move (1-3): ")

# Validate user input
if choice.isdigit():
    choice_int = int(choice)
    # Check if choice is within valid range
    if 1 <= choice_int <= len(moves):
        choice_move = moves[choice_int - 1]
        print(f"You chose {choice_move}.")
    else:
        print(f"Invalid choice. Please enter a number between 1 and {len(moves)}.")
else:
    print("Input is not valid. Please enter a number.")

def input_choice(choices: list[str]) -> int | None:
    """
    Get and validate user input for move selection.
    
    Args:
        choices: List of available moves
    
    Returns:
        int: Valid move index (1-based)
        None: If input is invalid
    """
    choice = input("Select a move (1-3): ")
    
    # Validate if input is a number
    if choice.isdigit():
        choice_int = int(choice)
        # Check if choice is within valid range
        if 1 <= choice_int <= len(choices):
            return choice_int
        else:
            print(f"Invalid choice. Please enter a number between 1 and {len(choices)}.")
    else:
        print("Input is not valid. Please enter a number.")
    return None

#any variable with uppercase is a constant
