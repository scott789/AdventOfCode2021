def calculate(file_name):
    string_list = open(file_name).readlines()

    number_increases = 0

    for i in range(0, len(string_list) - 1):
        string1 = string_list[i]
        string2 = string_list[i + 1]

        number1 = int(string1.rstrip())
        number2 = int(string2.rstrip())

        if number1 < number2:
            number_increases = number_increases + 1

    print(f'Increases: {number_increases}')


def main():
    calculate("day1-input")


main()
