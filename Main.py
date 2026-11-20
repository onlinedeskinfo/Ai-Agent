
# AI-AGENT
# Personal AI Assistant

def start_agent():
    print("\n==============================")
    print("       AI AGENT v1.0")
    print("==============================")
    print("Welcome! Your AI Agent is ready.")

    while True:
        print("\n1. Research")
        print("2. Content Creation")
        print("3. Cinematic Video")
        print("4. Automation")
        print("5. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            print("Research module coming soon!")

        elif choice == "2":
            print("Content Creation module coming soon!")

        elif choice == "3":
            print("Cinematic Video module coming soon!")

        elif choice == "4":
            print("Automation module coming soon!")

        elif choice == "5":
            print("AI Agent shutting down.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    start_agent()
      
