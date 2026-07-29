# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
def generate_fibonacci(n):
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    # Initialize the first two terms
    fib_sequence = [0, 1]

    # Use an iterative loop to generate remaining terms
    for i in range(2, n):
        next_term = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_term)

    return fib_sequence
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
def is_fibonacci(number):
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
    if number < 0:
        return False

    a, b = 0, 1

    
    while a < number:
        a, b = b, a + b

    
    return a == number
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).

if __name__ == "__main__":
    print("--- PART A: Fibonacci Sequence Generator ---")
    terms_input = int(input("How many terms? "))

    if terms_input <= 0:
        print("Error: Please enter a positive integer greater than 0.")
    else:
        fib_list = generate_fibonacci(terms_input)

        print("Fibonacci sequence:", end=" ")
        for num in fib_list:
            print(num, end=" ")
        print()  
    print("\n--- PART B: Fibonacci Number Checker ---")
    check_num = int(input("Enter a number to check: "))

    if is_fibonacci(check_num):
        print(check_num, "is a Fibonacci number.")
    else:
        print(check_num, "is NOT a Fibonacci number.")

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

