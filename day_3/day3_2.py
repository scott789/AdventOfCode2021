def number_of_bits_at_index(dictionary, bit_to_seek, col_ix):
    ret_val = 0

    for row_ix in range(0, len(dictionary)):
        binary_number = dictionary[row_ix]

        bit = binary_number[col_ix]

        if bit == bit_to_seek:
            ret_val += 1

    return ret_val


def calculate(file_name):
    rows = []
    with open(file_name) as file:
        for line in file:
            rows.append(line.rstrip())

    oxygen_generator_rating_bits = ''

    row_length = len(rows[0])

    for col_ix in range(0, row_length):
        count_0 = number_of_bits_at_index(rows, '0', col_ix)
        count_1 = number_of_bits_at_index(rows, '1', col_ix)
        bigger_number = 0 if count_0 > count_1 else 1

        for i, e in reversed(list(enumerate(rows))):
            if int(e[col_ix]) != bigger_number:
                if len(rows) > 1:
                    rows.pop(i)
                else:
                    oxygen_generator_rating_bits = e

    print(f'rows: {rows}')

    if oxygen_generator_rating_bits == '':
        oxygen_generator_rating_bits = rows[0]

    oxygen_generator_rating = int(oxygen_generator_rating_bits, 2)

    print(f'oxygen_generator_rating: {oxygen_generator_rating}')


def main():
    calculate("day3-input")


main()
