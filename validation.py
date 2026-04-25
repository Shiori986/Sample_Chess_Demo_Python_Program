import re

def check_global_command(text):
    """
    Checks if the input is a global command like quit/exit/menu.
    Returns:
      - "QUIT" if user wants to quit
      - "MENU" if user wants main menu
      - None otherwise
    """
    lowered = text.strip().lower()
    if lowered in ("quit", "exit"):
        return "QUIT"
    if lowered == "menu":
        return "MENU"
    return None


def get_valid_choice(prompt, valid_choices):
    """
    Repeatedly asks the user for input until they enter a valid choice.
    valid_choices should be a list of strings like ["1", "2", "3"].
    """
    while True:
        choice = input(prompt).strip()

        # Check for global commands
        cmd = check_global_command(choice)
        if cmd:
            return cmd

        if choice in valid_choices:
            return choice

        print(f"Invalid choice. Please enter one of: {', '.join(valid_choices)}")


def get_valid_name(prompt):
    """
    Accepts only human-like names:
    - Letters
    - Spaces
    - Hyphens
    - Apostrophes
    Rejects numbers and random strings.
    """
    pattern = r"^[A-Za-z][A-Za-z\s'\-]*[A-Za-z]$"

    while True:
        name = input(prompt).strip()

        # Check for global commands
        cmd = check_global_command(name)
        if cmd:
            return cmd

        if re.match(pattern, name):
            return name

        print("Invalid name. Please enter a real name (letters only).")


def get_valid_color(prompt):
    """
    Accepts:
    - W, w, White, white
    - B, b, Black, black
    Returns normalized 'white' or 'black'
    """
    while True:
        color = input(prompt).strip()

        # Check for global commands
        cmd = check_global_command(color)
        if cmd:
            return cmd

        lowered = color.lower()
        if lowered in ["w", "white"]:
            return "white"
        if lowered in ["b", "black"]:
            return "black"

        print("Invalid color. Enter W/White or B/Black.")