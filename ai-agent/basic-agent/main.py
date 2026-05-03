from llm import ask_ai
while True:
    user = input("You: ")

    if user == "exit":
        break

    if user.strip() == "":   # 👈 FIX
        print("Please type something...")
        continue

    answer = ask_ai(user)
    print("AI:", answer)