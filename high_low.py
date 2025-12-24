from game_data import data
from art import logo, vs
import random


def format_data(account):
    """Takes account data and returns a formatted string"""
    account_name = account["name"]
    account_description = account["description"]
    account_country =  account["location"]
    return f"{account_name} is a {account_description} from {account_country}."

def check_answer(user_guess, a_followers, b_followers):
    """Checks if the user guess is correct"""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

print(logo)
score = 0
continue_game = True
account_b = random.choice(data)

while continue_game:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"A: {format_data(account_a)}")
    print(vs)
    print(f"B: {format_data(account_b)}\n")

    guess = input("Who has more followers? (A/B): ").lower()
    print("\n" * 30)
    print(logo)

    a_followers = account_a["followers"]
    b_followers = account_b["followers"]
    is_correct = check_answer(guess, a_followers, b_followers)

    if is_correct:
        score += 1
        print(f"Correct! Current score: {score}")
    else:
        print("Incorrect! :(")
        print(f"Final score: {score}")
        continue_game = False

