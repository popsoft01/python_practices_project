import random


def guess_game():
    computer_guess = random.randint(1, 20)
    user_geuss = int(input("enter guess number"))

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


def build_profile(first, last, **user_info):
    profile = {"first_name": first, "last_name": last}
    for ket, value in user_info.items():
        profile[ket] = value
    return profile


def sand_wiches(**item):
    person = {}
    for key, value in item.items():
        person[key] = value
    return person


def car_info(name, power, **info):
    cars = {name: 'suberu', power: "frontWill"}
    for key, value in info.items():
        cars[key] = value
    return cars


# guess_game()
user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)
yes = sand_wiches(food="rice", cloth="ankara", box="black")
print(yes)
