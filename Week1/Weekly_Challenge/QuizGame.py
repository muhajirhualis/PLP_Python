# 2. Simple Quiz Game 🎮

# Create a multiple-choice quiz with questions about Python, movies, or any fun topic! Display scores at the end and allow the user to play again. 🏆

def run_quiz():

  quizzes = [
    {
      "question": "What is Python?",
      "choices": {"A": "Dynamically typed Programming Language", "B": "TypeScript framework"},
      "answer": "A"
    },
    {
        "question": "Why is Python popular in AI/ML?",
        "choices": {"A": "Many Libraries and Frameworks", "B": "It's the fastest language"},
        "answer": "A"
    },
    {
        "question": "Is Python easy to learn?",
        "choices": {"A": "Yes", "B": "No"},
        "answer": "A"
    }
  ]

  score = 0

  for q in quizzes:
    print(f"{q["question"]}")
    print(f"{q["choices"]}")
    
    answer = input("Choose Your Answer is A/B ?").strip().upper()

    if answer == q["answer"]:
      print("Correct Answer")
      score += 1
    else:
      print(f"Wrong Answer! The Correct Answer is {q['answer']}")
    
  print(f"Quiz Finished! Your Score is: {score} / {len(quizzes)}")

  play_again = input("Do you want to play again? Type Yes / No:").strip().lower()
  if play_again == "yes":
    run_quiz()
  else:
    print("Thanks for playing! 👋")


run_quiz()
