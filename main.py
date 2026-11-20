import os

def banner():
    print("\n" + "=" * 40)
    print("       AI AGENT - MANNU AI")
    print("=" * 40)

def research():
    topic = input("Enter research topic: ")
    print("Research module ready for:", topic)
    print("AI API integration will be added next.")

def content():
    topic = input("Enter content topic: ")
    print("Content creation module ready for:", topic)

def cinematic():
    topic = input("Enter video topic: ")
    print("Cinematic video project:", topic)

def automation():
    print("Automation module selected.")
    print("More features coming soon.")

def main():
    while True:
        banner()
        print("1. Research")
        print("2. Content Creation")
        print("3. Cinematic Video")
        print("4. Automation")
        print("5. Exit")

        choice = input("\nChoose option: ")

        if choice == "1":
            research()
        elif choice == "2":
            content()
        elif choice == "3":
            cinematic()
        elif choice == "4":
            automation()
        elif choice == "5":
            print("AI Agent Closed.")
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
