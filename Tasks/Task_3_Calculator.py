def get_inputs():
    number1 = int(input("Enter number 1: "))
    number2 = int(input("Enter number 2: "))
    return number1, number2

def addition(number1, number2):
    return f"{number1 + number2} is the result of addition."

def subtraction(number1, number2):
    return f"{number1 - number2} is the result of subtraction."

def multiplication(number1, number2):
    return f"{number1 * number2} is the result of multiplication."

def division(number1, number2):
    if number2 == 0:
        return "Error: Division by zero."
    else:
        return f"{number1 // number2} is the result of division."

def main():
    while True:
        print("\n1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            num1, num2 = get_inputs()
            print(addition(num1, num2))
        elif choice == 2:
            num1, num2 = get_inputs()
            print(subtraction(num1, num2))
        elif choice == 3:
            num1, num2 = get_inputs()
            print(multiplication(num1, num2))
        elif choice == 4:
            num1, num2 = get_inputs()
            print(division(num1, num2))
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
