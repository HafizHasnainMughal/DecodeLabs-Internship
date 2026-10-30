
# ==========================================
# Project 1: Rule-Based AI Chatbot
# Developed using Python
# ==========================================


def show_welcome():
    """Display the chatbot welcome screen."""
    print("\n" + "=" * 45)
    print("       WELCOME TO RULE-BASED AI CHATBOT")
    print("=" * 45)
    print("Hello! I am Rule-Based AI Chatbot, your virtual assistant.")
    print("Type 'help' to see available commands.")
    print("Type 'bye', 'exit', or 'quit' to stop.")
    print("-" * 45)


def show_help():
    """Display the available commands."""
    print("\n----------- HELP MENU -----------")
    print("1. Say Hello, Hi, Hey, or Salam")
    print("2. Ask: How are you?")
    print("3. Ask: What is your name?")
    print("4. Type: My name is Ali")
    print("5. Type: Bye, Exit, or Quit to stop")
    print("--------------------------------\n")


def get_response(message, user_name):
    """Generate responses using predefined rules."""

    # Normalize input: ignore case and extra spaces
    message = " ".join(message.lower().split())

    # Greeting rules
    if message in ["hi", "hello", "hey"]:
        return f"Hello, {user_name}! How can I help you?"

    elif message in [
        "salam",
        "assalam o alaikum",
        "assalam-o-alaikum",
        "assalamualaikum"
    ]:
        return f"Wa Alaikum Assalam, {user_name}!"

    # General conversation
    elif message in ["how are you", "how are you?"]:
        return "I am fine, thank you! How are you?"

    elif message in ["what is your name", "who are you"]:
        return "I am Rule-Based AI Chatbot, your virtual assistant."

    elif message in ["thank you", "thanks"]:
        return "You're welcome! Happy to help."

    # Help menu
    elif message in ["help", "menu", "commands"]:
        show_help()
        return None

    # Exit commands
    elif message in ["bye", "goodbye", "exit", "quit"]:
        return f"Goodbye, {user_name}! Have a great day."

    # Friendly fallback response
    else:
        return (
            "Sorry, I don't understand that yet.\n"
            "Please type 'help' to see what I can do."
        )


def main():
    """Run the chatbot in a continuous conversation loop."""

    show_welcome()

    user_name = input("Bot: What should I call you? ").strip()

    if not user_name:
        user_name = "Friend"

    print(f"\nBot: Nice to meet you, {user_name}!")
    print("Bot: Let's start chatting.\n")

    # Continuous loop
    while True:
        try:
            message = input(f"{user_name}: ").strip()

            # Handle empty input
            if not message:
                print("Bot: Please type a message.")
                continue

            # Allow the user to update their name
            normalized = " ".join(message.lower().split())

            if normalized.startswith("my name is "):
                new_name = message.strip()[11:].strip()

                if new_name:
                    user_name = new_name
                    print(f"Bot: Nice to meet you, {user_name}!")
                else:
                    print("Bot: Please enter your name.")
                continue

            # Get response based on rules
            response = get_response(message, user_name)

            if response is not None:
                print(f"Bot: {response}")

            # Stop the program on exit commands
            if normalized in ["bye", "goodbye", "exit", "quit"]:
                break

        except (KeyboardInterrupt, EOFError):
            print("\nBot: Chat ended. Goodbye!")
            break

    print("\nThank you for using Rule-Based AI Chatbot!")


# Program entry point
if __name__ == "__main__":
    main()
