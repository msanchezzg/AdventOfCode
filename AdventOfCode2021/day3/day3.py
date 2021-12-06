# -*- coding: utf-8 -*-


import argparse


MOST_COMMON = 0
LEAST_COMMON = 1


def bin_to_int(bin_str):
    return int(bin_str, 2)

def matches_bit(bin_str, bit_index, bit_value):
    return bin_str[bit_index] == bit_value

def get_common_bits(numbers, bit_index):
    number_len_half = len(numbers)/2
    bit_sum = sum([int(number[bit_index]) for number in numbers])
    if bit_sum >= number_len_half:
        return ('1','0')

    return ('0','1')

def get_bin_reducing_list(numbers, bit_index=0, criteria=MOST_COMMON):
    if len(numbers) == 0:
        return
    if len(numbers) == 1:
        return numbers[0]
    most_common, least_common = get_common_bits(numbers, bit_index)
    bit = most_common if criteria == MOST_COMMON else least_common
    new_numbers = list(filter(lambda num: matches_bit(num, bit_index, bit), numbers))

    return get_bin_reducing_list(new_numbers, bit_index+1, criteria)


def main(input_file):

    with open(input_file, "r") as f:
        numbers = [line for line in f.read().split('\n') if line]

    number_len = len(numbers[0])
    gamma = ''
    epsilon = ''

    for i in range(number_len):
        most_common_bit, least_common_bit = get_common_bits(numbers, i)
        gamma += most_common_bit
        epsilon += least_common_bit

    int_gamma = bin_to_int(gamma)
    int_epsilon = bin_to_int(epsilon)

    print('PART 1')
    print(f'Gamma rate: {gamma} = {int_gamma}')
    print(f'Epsilon rate: {epsilon} = {int_epsilon}')
    print(f'Product = {int_gamma * int_epsilon}')

    print('\n----------------------------------------------\n')

    oxygen = get_bin_reducing_list(numbers, criteria=MOST_COMMON)
    int_oxygen = bin_to_int(oxygen)

    co2 = get_bin_reducing_list(numbers, criteria=LEAST_COMMON)
    int_co2 = bin_to_int(co2)

    print('PART 2')
    print(f'Oxygen generator rating: {oxygen} = {int_oxygen}')
    print(f'CO2 scrubber rating rating: {co2} = {int_co2}')
    print(f'Product = {int_oxygen*int_co2}')



if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Python3 template file for Advent of Code problems"
    )
    parser.add_argument("input_file", type=str, help="File with problem input")

    args = parser.parse_args()
    main(args.input_file)
