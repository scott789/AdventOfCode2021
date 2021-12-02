def calculate(file_name):
    string_list = open(file_name).readlines()

    horizontal_position = 0
    depth = 0

    for i in range(0, len(string_list)):
        instructions = string_list[i].split()
        direction = instructions[0]
        distance = int(instructions[1])

        if direction == 'forward':
            horizontal_position = horizontal_position + distance
        elif direction == 'down':
            depth = depth + distance
        else:
            depth = depth - distance

    print(f'horizontal_position: {horizontal_position}')
    print(f'depth: {depth}')

    answer = horizontal_position * depth
    print(f'answer: {answer}')


def main():
    calculate("day2-input")


main()
