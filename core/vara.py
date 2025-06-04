import time

def main():
    print("Vara is alive.")
    while True:
        prompt = input("You > ")
        if prompt.lower() in ["exit", "quit"]:
            break
        print("Vara >", respond(prompt))

def respond(text):
    return f"Signal received: '{text}'"

if __name__ == "__main__":
    main()
