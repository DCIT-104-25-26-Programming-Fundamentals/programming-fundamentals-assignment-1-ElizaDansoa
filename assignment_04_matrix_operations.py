# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
def print_matrix(matrix):
    """Prints a 2D list in a formatted grid."""
    for row in matrix:
        for element in row:
            
            print(str(element).rjust(4), end=" ")
        print() 

def read_matrix(rows, cols):
    
    matrix = []
    for i in range(rows):
        row_input = input("Enter row " + str(i + 1) + ": ")
        # Split input string by spaces and convert each value to int
        row = [int(val) for val in row_input.split()]
        matrix.append(row)
    return matrix
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).

def transpose_matrix(matrix):
   
    rows = len(matrix)
    cols = len(matrix[0])

    
    transposed = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transposed.append(new_row)

    return transposed
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
def add_matrices(matrix_a, matrix_b):
    
    rows = len(matrix_a)
    cols = len(matrix_a[0])

    result = []
    for i in range(rows):
        new_row = []
        for j in range(cols):
            new_row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(new_row)

    return result
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
def multiply_matrices(matrix_a, matrix_b):
    
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0]) 
    cols_b = len(matrix_b[0])

    
    result = []
    for i in range(rows_a):
        row = [0] * cols_b
        result.append(row)

    
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]

    return result
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
if __name__ == "__main__":
    print("--- PART A: Transpose Matrix ---")
    m = int(input("Enter number of rows: "))
    n = int(input("Enter number of columns: "))
    
    print("Enter Matrix values:")
    mat_a = read_matrix(m, n)

    print("\nOriginal Matrix:")
    print_matrix(mat_a)

    transposed_mat = transpose_matrix(mat_a)
    print("\nTransposed Matrix:")
    print_matrix(transposed_mat)

    print("\n--- PART B: Matrix Addition ---")
    print("Reading second matrix of size", m, "x", n, "for addition:")
    mat_b = read_matrix(m, n)

    added_mat = add_matrices(mat_a, mat_b)
    print("\nSum of Matrix A and Matrix B:")
    print_matrix(added_mat)

    print("\n--- PART C: Matrix Multiplication ---")
    print("To multiply Matrix A (" + str(m) + "x" + str(n) + "), enter Matrix C with " + str(n) + " rows.")
    p = int(input("Enter number of columns for Matrix C: "))
    mat_c = read_matrix(n, p)

    multiplied_mat = multiply_matrices(mat_a, mat_c)
    print("\nProduct of Matrix A and Matrix C:")
    print_matrix(multiplied_mat)

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

