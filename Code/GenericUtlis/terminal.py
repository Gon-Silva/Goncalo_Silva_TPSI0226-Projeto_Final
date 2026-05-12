# Clean the terminal
def cls():
    print("\033c", end="")
    # Move the cursor to the home position
    # Clear both the screen and the scrollback buffer
    # Perform a complete terminal reset


# Waits for the user to press a button or for two seconds to pass
def press_to_continue():
    input("\nPress [ENTER] to continue...")
