def ai_guess_number():
    print("Think of a number between 1 and 100. The AI will try to guess it!")
    low = 1
    high = 100
    attempts = 0

    while low <= high:
        guess = (low + high) // 2
        attempts += 1
        print(f"AI guesses: {guess}")
        feedback = input("Is your number higher, lower, or correct? ").lower()
        
        if feedback == "correct":
            print(f"AI guessed your number {guess} in {attempts} tries!")
            break
        elif feedback == "higher":
            low = guess + 1
        elif feedback == "lower":
            high = guess - 1
        else:
            print("Please respond with 'higher', 'lower', or 'correct'.")

if __name__ == "__main__":
    ai_guess_number()
