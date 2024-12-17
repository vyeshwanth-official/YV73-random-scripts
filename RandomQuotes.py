import random
import os
import sys

# List of motivational quotes
quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "Your limitation—it's only your imagination.",
    "Push yourself, because no one else is going to do it for you.",
    "Great things never come from comfort zones.",
    "Dream it. Wish it. Do it.",
    "Success doesn’t just find you. You have to go out and get it.",
    "The harder you work for something, the greater you’ll feel when you achieve it.",
    "Dream bigger. Do bigger.",
    "Don’t stop when you’re tired. Stop when you’re done.",
]

def clear_screen():
    # Clear the console screen (works on both Windows and Unix-based systems)
    if sys.platform.startswith('win'):
        os.system('cls')  # For Windows
    else:
        os.system('clear')  # For Linux or macOS

def display_random_quote():
    # Pick a random quote
    quote = random.choice(quotes)
    clear_screen()  # Clear the screen before displaying the new quote
    print(f"\n{quote}\n")

def main():
    print("Press any key to get a motivational quote, or press 'q' to quit.")
    while True:
        user_input = input("Press Enter to get a new quote (or 'q' to quit): ")
        if user_input.lower() == 'q':
            print("Goodbye! Stay motivated!")
            break
        else:
            display_random_quote()

if __name__ == "__main__":
    main()
