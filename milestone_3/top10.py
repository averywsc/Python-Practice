# === Functions ===

def normalize_input(text):
    return text.strip().lower()

def check_guess(guess, top_10_answers, guessed_correctly):
    normalized_guess = normalize_input(guess)
    for answer in top_10_answers:
        if normalize_input(answer) == normalized_guess and answer not in guessed_correctly:
            return True, answer
    return False, None

def display_results(correct_guesses, top_10_answers):
    missed_answers = [answer for answer in top_10_answers if answer not in correct_guesses]
    print("\n🎯 Quiz Over! Here's how you did:")
    print(f"✅ Correct guesses: {len(correct_guesses)}/10\n")
    
    print("🟢 You got:")
    for guess in correct_guesses:
        print(f" - {guess}")

    print("\n🔴 You missed:")
    for miss in missed_answers:
        print(f" - {miss}")

def start_quiz(question, top_10_answers):
    print(f"🔟 {question}")
    print("Type 'quit' to stop the quiz early.\n")

    guessed_correctly = []

    while len(guessed_correctly) < 10:
        guess = input("Your guess: ")
        if guess.lower() == 'quit':
            break

        is_correct, normalized_answer = check_guess(guess, top_10_answers, guessed_correctly)
        if is_correct:
            guessed_correctly.append(normalized_answer)
            print("✅ Correct!")
        else:
            print("❌ Not on the list or already guessed.")

    display_results(guessed_correctly, top_10_answers)


# === Example Usage ===

if __name__ == "__main__":
    top_10_movies = [
        "Avatar",
        "Avengers: Endgame",
        "Titanic",
        "Star Wars: The Force Awakens",
        "Avengers: Infinity War",
        "Spider-Man: No Way Home",
        "Jurassic World",
        "The Lion King (2019)",
        "The Avengers",
        "Furious 7"
    ]

    start_quiz("Name the Top 10 highest-grossing movies of all time (as of 2025):", top_10_movies)


