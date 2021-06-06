import random
import string

password_length = int(input('what is the length of your password'))


def password_generator():
    password = " "
    for x in range(0, 4):
        password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(
            string.digits) + random.choice(string.punctuation)
        for letter in range(password_length - 4):
            password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
            print(password)

def email_generator():
    first_name = input("enter the first name")
    last_name = input("enter you last name")
    email_gen = first_name[0] + "-" +last_name + "@semicolon.com"
    print(email_gen)

password_generator()
email_generator()