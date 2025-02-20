def introduction():
    print("This program converts numbers between binary, decimal, hexadecimal, and octal.")
    print("You can keep converting numbers until you decide to exit.")

def decimal_to_binary():
    while True:
        num = input("Enter a decimal number: ")
        if num.isdigit():
            print("Binary:", bin(int(num))[2:])
            break
        print("Invalid input. Please enter a valid decimal number.")

def binary_to_decimal():
    while True:
        num = input("Enter a binary number: ")
        if all(c in '01' for c in num):
            print("Decimal:", int(num, 2))
            break
        print("Invalid input. Please enter a valid binary number.")

def decimal_to_hexadecimal():
    while True:
        num = input("Enter a decimal number: ")
        if num.isdigit():
            print("Hexadecimal:", hex(int(num))[2:])
            break
        print("Invalid input. Please enter a valid decimal number.")

def decimal_to_octal():
    while True:
        num = input("Enter a decimal number: ")
        if num.isdigit():
            print("Octal:", oct(int(num))[2:])
            break
        print("Invalid input. Please enter a valid decimal number.")

def main():
    introduction()
    while True:
        choice = input("Convert (1) Decimal to Binary, (2) Binary to Decimal, (3) Decimal to Hexadecimal, (4) Decimal to Octal? (Type 'exit' to stop): ").strip().lower()
        if choice == "1":
            decimal_to_binary()
        elif choice == "2":
            binary_to_decimal()
        elif choice == "3":
            decimal_to_hexadecimal()
        elif choice == "4":
            decimal_to_octal()
        elif choice == "exit":
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 'exit'.")
    print("Thanks for using the program!")

main()
