print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst Number")
    if first_number == 'w':
        break
    second_number = input("\nSecond Number")
    if second_number == 'w':
        break
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("Zero division lailai")
    else:
        print(answer)