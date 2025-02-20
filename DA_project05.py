def introduction():
    print("This program adds two numbers.")
    print("You can keep adding numbers until you decide to exit.")

def get_number(prompt):
    while True:
        num = input(prompt)
        if num.isdigit():
            return int(num)
        print("Invalid input. Please enter a whole number.")

def main():
    introduction()
    while True:
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")
        print("The sum is:", num1 + num2)
        again = input("Do you want to add more numbers? (yes/no): ").strip().lower()
        if again == "no":
            break
    print("Thanks for using the program!")

main()
