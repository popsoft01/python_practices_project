import random

computer_guess = random.randint(1, 20)
user_geuss = int(input("enter guess number"))


def guess_game():
    try:
        if user_geuss == computer_guess:
            print(f"Congratulations {computer_guess}")
        elif user_geuss > computer_guess:
            print(f"guess too high try again {computer_guess}")
        elif user_geuss < computer_guess:
            print(f"guess number too low try again {computer_guess}")
    except ValueError:
        print("input can not be empty")
        guess_game()


guess_game()
