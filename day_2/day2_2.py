def calculate(file_name):
    string_list = open(file_name).readlines()

    horizontal_position = 0
    depth = 0
    aim = 0

    for i in range(0, len(string_list)):
        instructions = string_list[i].split()
        direction = instructions[0]
        x = int(instructions[1])

        if direction == 'forward':
            horizontal_position = horizontal_position + x
            depth = depth + (x * aim)
        elif direction == 'down':
            aim = aim + x
        elif direction == 'up':
            aim = aim - x
        else:
            print("invalid")

    print(f'horizontal_position: {horizontal_position}')
    print(f'depth: {depth}')
    print(f'aim: {aim}')

    answer = horizontal_position * depth
    print(f'answer: {answer}')


def main():
    calculate("day2-input")


main()
