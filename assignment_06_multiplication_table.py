# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
def print_single_table(number):
# Write a Python program that generates multiplication tables using loops
# and functions.
    
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Print the multiplication table for that number from 1 to 12.
#print("\nMultiplication Table for " + str(number) + ":")
    for i in range(1, 13):
        result = number * i
        
        print(str(number) + " x " + str(i).rjust(2) + " = " + str(result))
# Expected output (if user enters 5):
#
#   Multiplication Table for 5:
#   5  x  1  =  5
#   5  x  2  =  10
#   5  x  3  =  15
#   ...
#   5  x  12 =  60
#
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
# - Ask the user to enter a number N.
# - Print the full multiplication table for every number from 1 to N.
# - Add a separator line (e.g. "---") between each table.
def print_tables_up_to_n(n):
    
    for current_num in range(1, n + 1):
        print_single_table(current_num)
        print("---------------------------")
# Expected output (if user enters 3):
#
#   Multiplication Table for 1:
#   1  x  1  =  1
#   ...
#   1  x  12 =  12
#   ---------------------------
#   Multiplication Table for 2:
#   2  x  1  =  2
#   ...
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
# - Complete Part A before attempting Part B.

if __name__ == "__main__":
    print("--- PART A: Single Multiplication Table ---")
    num_input = int(input("Enter a number: "))
    
   
    if num_input <= 0:
        print("Error: Please enter a positive integer greater than 0.")
    else:
        print_single_table(num_input)

    print("\n--- PART B: Tables from 1 to N ---")
    n_input = int(input("Enter N to print tables up to N: "))
    
    
    if n_input <= 0:
        print("Error: Please enter a positive integer greater than 0.")
    else:
        print_tables_up_to_n(n_input)

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

