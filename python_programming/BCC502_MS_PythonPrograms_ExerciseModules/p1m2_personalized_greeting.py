"""Part 1, Module 2: Create a personalized greeting."""


def build_greeting(raw_name):
    """Clean up a name and return a personalized greeting."""
    name = raw_name.strip().title()
    return f"Hello, {name}! Welcome to Python."


def main():
    raw_name = input("What is your name? ")
    print(build_greeting(raw_name))
    print(f"Your name has {len(raw_name.strip())} characters.")


if __name__ == "__main__":
    main()
