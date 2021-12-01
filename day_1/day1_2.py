def calculate(file_name):
    string_list = open(file_name).readlines()

    number_increases = 0

    for i in range(0, len(string_list) - 3):
        string1 = string_list[i]
        string2 = string_list[i + 1]
        string3 = string_list[i + 2]
        string4 = string_list[i + 3]

        number1 = int(string1.rstrip())
        number2 = int(string2.rstrip())
        number3 = int(string3.rstrip())
        number4 = int(string4.rstrip())

        sum1 = number1 + number2 + number3
        sum2 = number2 + number3 + number4

        if sum1 < sum2:
            number_increases = number_increases + 1

    print(f'Sliding Increases: {number_increases}')


def main():
    calculate("day1-input")


main()
