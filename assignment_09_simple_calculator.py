# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
def add(a, b):
   
    return a + b


def subtract(a, b):
    
    return a - b


def multiply(a, b):
    
    return a * b


def divide(a, b):
   
    if b == 0:
        return None
    return round(a / b, 2)


def modulus(a, b):
    
    if b == 0:
        return None
    return a % b


def exponentiate(a, b):
    
    return a ** b
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
def show_menu():
    
    
    print("      SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
def get_numbers():
    
    num1 = float(input("Enter first number : "))
    num2 = float(input("Enter second number: "))
    return num1, num2
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
if __name__ == "__main__":
    while True:
        show_menu()
        choice = input("Select an operation (1-7): ")

        if choice == "7":
            print("\nGoodbye!")
            break

        if choice in ["1", "2", "3", "4", "5", "6"]:
            try:
                num1, num2 = get_numbers()
                
                
                n1_str = str(int(num1)) if num1.is_integer() else str(num1)
                n2_str = str(int(num2)) if num2.is_integer() else str(num2)

                if choice == "1":
                    res = add(num1, num2)
                    res_str = str(int(res)) if isinstance(res, (int, float)) and res.is_integer() else str(res)
                    print("Result:", n1_str, "+", n2_str, "=", res_str)

                elif choice == "2":
                    res = subtract(num1, num2)
                    res_str = str(int(res)) if isinstance(res, (int, float)) and res.is_integer() else str(res)
                    print("Result:", n1_str, "-", n2_str, "=", res_str)

                elif choice == "3":
                    res = multiply(num1, num2)
                    res_str = str(int(res)) if isinstance(res, (int, float)) and res.is_integer() else str(res)
                    print("Result:", n1_str, "*", n2_str, "=", res_str)

                elif choice == "4":
                    res = divide(num1, num2)
                    if res is None:
                        print("Error: Cannot divide by zero.")
                    else:
                        print("Result:", n1_str, "/", n2_str, "=", res)

                elif choice == "5":
                    res = modulus(num1, num2)
                    if res is None:
                        print("Error: Cannot perform modulus by zero.")
                    else:
                        res_str = str(int(res)) if isinstance(res, (int, float)) and res.is_integer() else str(res)
                        print("Result:", n1_str, "%", n2_str, "=", res_str)

                elif choice == "6":
                    res = exponentiate(num1, num2)
                    res_str = str(int(res)) if isinstance(res, (int, float)) and res.is_integer() else str(res)
                    print("Result:", n1_str, "**", n2_str, "=", res_str)

            except ValueError:
                print("Error: Please enter valid numerical values.")
        else:
            print("Error: Invalid selection. Please choose a number from 1 to 7.")

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

