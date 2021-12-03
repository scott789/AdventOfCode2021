def create_or_increment(dictionary, index):
    if index in dictionary:
        dictionary[index] = dictionary[index] + 1
    else:
        dictionary[index] = 1


def calculate(file_name):
    gamma_rate_bits = ''
    epsilon_rate_bits = ''

    rows = []
    with open(file_name) as file:
        for line in file:
            rows.append(line.rstrip())

    count_0_at_column = {}
    count_1_at_column = {}

    for row_ix in range(0, len(rows)):
        binary_number = rows[row_ix]

        for col_ix in range(0, len(rows[row_ix])):
            bit = binary_number[col_ix]

            if bit == '0':
                create_or_increment(count_0_at_column, col_ix)
            elif bit == '1':
                create_or_increment(count_1_at_column, col_ix)
            else:
                print('INVALID')

    for i in range(0, len(count_0_at_column)):
        if count_0_at_column.get(i) > count_1_at_column.get(i):
            gamma_rate_bits += '0'
            epsilon_rate_bits += '1'
        else:
            gamma_rate_bits += '1'
            epsilon_rate_bits += '0'

    # Sum up the counts
    gamma = int(gamma_rate_bits, 2)
    epsilon = int(epsilon_rate_bits, 2)
    answer = gamma * epsilon

    print(f'gamma_rate: {gamma}')
    print(f'epsilon_rate: {epsilon}')
    print(f'answer: {answer}')


def main():
    calculate("day3-input")


main()
