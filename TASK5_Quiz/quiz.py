import random

# Quiz questions with options and correct answers
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["a) London", "b) Paris", "c) Rome", "d) Madrid"],
        "correct_answer": "b",
    },
    {
        "question": "Which planet is known as the 'Red Planet'?",
        "options": ["a) Mars", "b) Venus", "c) Jupiter", "d) Saturn"],
        "correct_answer": "a",
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["a) Elephant", "b) Blue Whale", "c) Giraffe", "d) Gorilla"],
        "correct_answer": "b",
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["a) Pablo Picasso", "b) Vincent van Gogh", "c) Leonardo da Vinci", "d) Michelangelo"],
        "correct_answer": "c",
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["a) H2O", "b) CO2", "c) O2", "d) NaCl"],
        "correct_answer": "a",
    },
]

def display_welcome_message():
    print("Welcome to the Quiz Game!")
    print("Answer multiple-choice or fill-in-the-blank questions on a specific topic.")
    print("Let's see how well you can do!\n")

def display_question(question_data):
    print(question_data["question"])
    for option in question_data["options"]:
        print(option)
    print()

def get_user_answer():
    user_answer = input("Enter the letter corresponding to your answer: ")
    return user_answer.lower()

def evaluate_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        print("Correct answer!")
        return True
    else:
        print("Incorrect answer. The correct answer is:", correct_answer.upper())
        return False

def calculate_final_score(score, total_questions):
    return (score / total_questions) * 100

def display_final_results(score, total_questions):
    percentage_score = calculate_final_score(score, total_questions)
    print("\n----- Final Results -----")
    print("Total Questions: ", total_questions)
    print("Your Score: ", score, "/", total_questions)
    print("Percentage Score: {:.2f}%".format(percentage_score))

def play_again():
    play_again_input = input("\nDo you want to play again? (yes/no): ")
    return play_again_input.lower() == "yes"

def main():
    display_welcome_message()
    total_questions = len(quiz_questions)
    score = 0

    while True:
        random.shuffle(quiz_questions)

        for i, question_data in enumerate(quiz_questions):
            display_question(question_data)
            user_answer = get_user_answer()

            if evaluate_answer(user_answer, question_data["correct_answer"]):
                score += 1

            print("\n------------------------\n")

        display_final_results(score, total_questions)

        if not play_again():
            break

        print("\n------------------------\n")
        score = 0

if __name__ == "__main__":
    main()
