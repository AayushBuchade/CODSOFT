def show_menu():
    print("\n" + "=" * 36)
    print("        PYTHON CALCULATOR")
    print("=" * 36)
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    print("=" * 30)


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "❌ Error: Division by zero is not allowed."
    return a / b


while True:
    show_menu()
    choice = input("Choose an operation (1-5): ")

    if choice == '5':
        print("\n✅ Thank you for using the calculator. Goodbye!")
        break

    if choice not in ['1', '2', '3', '4']:
        print("❌ Invalid choice! Please select a valid option.")
        continue

    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")

    if choice == '1':
        result = add(num1, num2)
        operation = "+"

    elif choice == '2':
        result = subtract(num1, num2)
        operation = "-"

    elif choice == '3':
        result = multiply(num1, num2)
        operation = "*"

    elif choice == '4':
        result = divide(num1, num2)
        operation = "/"

    print(f"\n📌 Result: {num1} {operation} {num2} = {result}")
