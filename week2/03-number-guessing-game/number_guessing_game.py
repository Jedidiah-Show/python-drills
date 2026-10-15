import random

def play_game(target=None, max_attempts=None):
    # Write your code here
    def play_on():
        to_continue = input("Would you like to continue (y/n): ").strip()
        if to_continue[0].lower() == "y":
            play_game(target=None, max_attempts=None)
        else:
            return attempts
    if target is None:
        target = random.randint(1, 101)
    attempts, user_guess = 0, 0
    while user_guess != target and attempts != max_attempts:
        user_guess = input("Enter your guess (1-100): ").strip()
        try:
            user_guess = int(user_guess)
            if user_guess < 1 or user_guess > 100:
                print("invalid input. enter a whole number between 1 and 100.")
                continue
            if user_guess < target:
                print("too low")
                attempts += 1
            elif user_guess > target:
                print("too high")
                attempts += 1
            elif user_guess == target:
                attempts += 1
                print(f"correct! you got it in {attempts} guesses")
                play_on()
        except ValueError:
            print("invalid input. enter a whole number between 1 and 100.")
    if max_attempts:
        print(f"You are out of guesses the target is {target}")
        play_on()
    return attempts

# Do not modify below this line
if __name__ == "__main__":
    play_game()
