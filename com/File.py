def file_reading():
    filename = open.txt
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        print(contents)


def file_with_path():
    filename = open.txt
    try:
        with open('desktop/oppen.txt') as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        print(contents)


file_reading()
file_with_path()
