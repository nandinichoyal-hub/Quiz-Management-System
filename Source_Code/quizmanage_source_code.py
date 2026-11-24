# ==========================================
#       QUIZ MANAGEMENT SYSTEM
#       Micro Project - I (Milestone 4: Optimised Version)
# ==========================================


# Question bank: created once when the program starts
QUESTIONS = [
    {
        "question": "What does AI stand for?",
        "options": [
            "A. Automated Internet",
            "B. Artificial Intelligence",
            "C. Advanced Information",
            "D. Artificial Internet"
        ],
        "answer": "B"
    },
    {
        "question": "Which language is commonly used in AI and Machine Learning?",
        "options": [
            "A. Python",
            "B. HTML",
            "C. CSS",
            "D. SQL"
        ],
        "answer": "A"
    },
    {
        "question": "Which of the following is a programming language?",
        "options": [
            "A. Python",
            "B. Windows",
            "C. Google",
            "D. Chrome"
        ],
        "answer": "A"
    },
    {
        "question": "What is the brain of a computer called?",
        "options": [
            "A. RAM",
            "B. Hard Disk",
            "C. CPU",
            "D. Keyboard"
        ],
        "answer": "C"
    },
    {
        "question": "Which data type is used for whole numbers in Python?",
        "options": [
            "A. float",
            "B. int",
            "C. string",
            "D. list"
        ],
        "answer": "B"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": [
            "A. //",
            "B. /* */",
            "C. #",
            "D. --"
        ],
        "answer": "C"
    },
    {
        "question": "What is the output of 5 + 3?",
        "options": [
            "A. 6",
            "B. 7",
            "C. 8",
            "D. 9"
        ],
        "answer": "C"
    },
    {
        "question": "Which function is used to display output in Python?",
        "options": [
            "A. input()",
            "B. print()",
            "C. display()",
            "D. output()"
        ],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": [
            "A. function",
            "B. define",
            "C. fun",
            "D. def"
        ],
        "answer": "D"
    },
    {
        "question": "Which of these is used to take input from the user in Python?",
        "options": [
            "A. scan()",
            "B. input()",
            "C. get()",
            "D. read()"
        ],
        "answer": "B"
    }
]


# Function to display the main menu
def display_menu():
    print("\n================================")
    print("       QUIZ MANAGEMENT SYSTEM")
    print("================================")
    print("1. Start Quiz")
    print("2. View Instructions")
    print("3. Exit")
    print("================================")


# Function to display quiz instructions
def show_instructions():
    print("\n========== INSTRUCTIONS ==========")
    print("1. The quiz contains 10 questions.")
    print("2. Each question has 4 options.")
    print("3. Enter A, B, C, or D as your answer.")
    print("4. Each correct answer gives 1 mark.")
    print("5. No negative marking.")
    print("6. Your final score will be displayed.")
    print("==================================")


# Function to calculate grade
def get_grade(percentage):
    # Returns the grade and performance message for a percentage

    if percentage >= 80:
        return "A", "Excellent!"

    elif percentage >= 60:
        return "B", "Very Good!"

    elif percentage >= 40:
        return "C", "Good!"

    return "D", "Needs Improvement."


# Function to evaluate quiz result
def evaluate_result(score, total_questions):

    # Avoid division by zero if there are no questions
    if total_questions == 0:
        percentage = 0
    else:
        percentage = (score / total_questions) * 100

    grade, performance = get_grade(percentage)

    print("\n========== QUIZ RESULT ==========")
    print("Total Questions :", total_questions)
    print("Correct Answers :", score)
    print("Wrong Answers   :", total_questions - score)
    print("Score           :", score, "/", total_questions)
    print(f"Percentage      : {percentage:.2f} %")
    print("Grade           :", grade)
    print("Performance     :", performance)
    print("================================")


# Function to get valid answer from user
def get_valid_answer():

    # Keeps asking until the user enters A, B, C or D
    while True:
        user_answer = input("Enter your answer (A/B/C/D): ").strip().upper()

        if user_answer in ("A", "B", "C", "D"):
            return user_answer

        print("Invalid input! Please enter A, B, C, or D.")


# Function to start the quiz
def start_quiz():

    score = 0

    print("\n================================")
    print("          STARTING QUIZ")
    print("================================")

    for index, question in enumerate(QUESTIONS, start=1):

        print("\nQuestion", index, "of", len(QUESTIONS))
        print(question["question"])

        for option in question["options"]:
            print(option)

        user_answer = get_valid_answer()

        if user_answer == question["answer"]:
            print("Correct Answer!")
            score += 1

        else:
            print("Wrong Answer!")
            print("Correct Answer:", question["answer"])

    evaluate_result(score, len(QUESTIONS))


# Main function
def main():

    print("Welcome to Quiz Management System!")

    try:
        while True:

            display_menu()

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                start_quiz()

            elif choice == "2":
                show_instructions()

            elif choice == "3":
                print("\nThank you for using Quiz Management System!")
                print("Goodbye!")
                break

            else:
                print("\nInvalid choice! Please select 1, 2, or 3.")

    except (EOFError, KeyboardInterrupt):
        print("\n\nInput ended. Exiting Quiz Management System. Goodbye!")


# Program execution starts here
if __name__ == "__main__":
    main()