# calculator.py
#deva maanas

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y
def division (x,y):
    return x/y

def multiply(x, y):
    return x * y

if __name__ == "__main__":
    while True:
        print("\nSimple Calculator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == '5':
            print("Exiting... Thank you!")
            break

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        
        else:
            print("Invalid input! Please enter a valid option.")
