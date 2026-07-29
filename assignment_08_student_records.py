# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
def show_menu():
    
    print("   STUDENT RECORD SYSTEM MENU")
    print("================================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")
# Build a console-based program that stores and manages student information.
# Each student record must contain:
#
#   - Name   : the student's full name (text)
#   - ID     : a unique student ID number (e.g. 20240001)
#   - Scores : a list of scores from multiple assessments (e.g. [75, 88, 90])
def compute_average(scores):
    """Calculates average score rounded to 2 decimal places."""
    if not scores:
        return 0.0
    
    total = 0
    for score in scores:
        total += score
    return round(total / len(scores), 2)
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Student
#      - Ask the user to enter the student's name and ID.
#      - Ask how many scores to enter, then collect each score one by one.
#      - Save the student record and confirm it was added.
def add_student(students):
    
    name = input("Student name: ")
    student_id = input("Student ID: ")
    
    try:
        num_scores = int(input("How many scores? "))
        if num_scores <= 0:
            print("Error: Number of scores must be greater than 0.")
            return
    except ValueError:
        print("Error: Invalid number entered.")
        return

    scores = []
    for i in range(1, num_scores + 1):
        try:
            score = float(input("Enter score " + str(i) + ": "))
            scores.append(score)
        except ValueError:
            print("Error: Invalid score. Setting score to 0.")
            scores.append(0.0)

    student = {
        "name": name,
        "id": student_id,
        "scores": scores
    }
    
    students.append(student)
    print('Student "' + name + '" added successfully.')
#   2. Display All Students
#      - Print a formatted table showing every student's:
#          Name, ID, individual scores, and their average score.
#      - If no students have been added yet, print a message saying so.
def display_students(students):
    if not students:
        print("\nNo student records available.")
        return

    print("\n--------------------------------------------------")
    print("Name".ljust(15) + "ID".ljust(12) + "Scores".ljust(15) + "Average")
    print("--------------------------------------------------")

    for student in students:
        scores_str = ", ".join(str(int(s) if s.is_integer() else s) for s in student["scores"])
        avg = compute_average(student["scores"])
        
        print(
            student["name"].ljust(15) +
            str(student["id"]).ljust(12) +
            scores_str.ljust(15) +
            str(avg)
        )
    print("--------------------------------------------------")
#   3. Calculate Average Score for a Specific Student
#      - Ask the user to enter a student ID.
#      - Find the student and calculate the average of their scores.
#      - Display the result. If the ID is not found, print an error message.
def calculate_student_average(students):
    if not students:
        print("\nNo student records available.")
        return

    search_id = input("Enter student ID: ")
    
    for student in students:
        if str(student["id"]) == str(search_id):
            avg = compute_average(student["scores"])
            print(student["name"] + "'s average score: " + str(avg))
            return

    print("Error: Student ID '" + search_id + "' not found.")
#   4. Quit
#      - End the program.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ================================
#      STUDENT RECORD SYSTEM MENU
#   ================================
#   1. Add student
#   2. Display all students
#   3. Calculate average score
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Student name: Alice Mensah
#   Student ID: 20240001
#   How many scores? 3
#   Enter score 1: 78
#   Enter score 2: 85
#   Enter score 3: 90
#   Student "Alice Mensah" added successfully.
#
#   Enter your choice (1-4): 2
#   --------------------------------------------------
#   Name           ID          Scores         Average
#   --------------------------------------------------
#   Alice Mensah   20240001    78, 85, 90     84.33
#   --------------------------------------------------
#
#   Enter your choice (1-4): 3
#   Enter student ID: 20240001
#   Alice Mensah's average score: 84.33
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store all student records in a list of dictionaries.
#   Example structure:
#       student = {
#           "name": "Alice Mensah",
#           "id": 20240001,
#           "scores": [78, 85, 90]
#       }
# - Average scores should be rounded to 2 decimal places.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices and missing student IDs gracefully.
if __name__ == "__main__":
    student_records = []

    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_student(student_records)
        elif choice == "2":
            display_students(student_records)
        elif choice == "3":
            calculate_student_average(student_records)
        elif choice == "4":
            print("\nGoodbye!")
            break
        else:
            print("Error: Invalid choice. Please enter a number from 1 to 4.")

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

