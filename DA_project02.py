def introduction():
    print("Welcome to the interactive question program!")
    print("You can answer the questions as many times as you like. Type 'exit' to stop.")

def ask_questions():
    questions = [
        "What is your favorite color? ",
        "What is your favorite food? ",
        "What is your favorite hobby? ",
        "What is your dream destination? "
    ]
    count = 0
    while True:
        question = questions[count % len(questions)]
        user_input = input(question).strip().lower()
        if user_input == "exit":
            break
        count += 1
    return count

def closing_statement(count):
    print("Thank you for participating! You answered", count, "questions.")

introduction()
total_questions = ask_questions()
closing_statement(total_questions)
