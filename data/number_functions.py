NUMBER_FILE = "number.txt"

def reset_number():
    with open(NUMBER_FILE, "w") as file:
        file.write("0")

def get_number():
    with open(NUMBER_FILE, "r") as file:
        number = str(int(file.read()) + 1)
    with open(NUMBER_FILE, "w") as file:
        file.write(number)
    return number
