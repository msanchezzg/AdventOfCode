from functools import reduce


def xor(a, b):
    return a ^ b

def get_knoth_hash_lengths(string):
    suffix = [17, 31, 73, 47, 23]
    # Convert characters to bytes using their ASCII codes
    return [ord(c) for c in string] + suffix

def knot_hash(string, num_elements=256):
    group_len = 16
    lengths = get_knoth_hash_lengths(string)
    numbers = knot_hash_loop(num_elements, lengths, 64)
    sparse_hash = [
        numbers[ngroup*group_len:ngroup*group_len+group_len]
        for ngroup in range(group_len)]
    dense_hash = [reduce(xor, group) for group in sparse_hash]
    hex_str = ''.join([f'{n:0>2X}' for n in dense_hash])

    return hex_str


def knot_hash_loop(num_elements, lengths, num_iterations):
    current_position = 0
    skip_size = 0
    numbers = list(range(num_elements))

    for _ in range(num_iterations):
        for length in lengths:
            # Reverse the order of that length of elements in the list, starting with the element at the current position.
            sublist = []
            for i in range(current_position, current_position+length):
                sublist.append(numbers[i]) if i < num_elements else sublist.append(numbers[i%num_elements])

            sublist_reversed = sublist[::-1]
            for i in range(current_position, current_position+length):
                k = i % num_elements if i >= num_elements else i
                numbers[k] = sublist_reversed[i-current_position]

            # Move the current position forward by that length plus the skip size.
            current_position = (current_position + length + skip_size) % num_elements

            # Increase the skip size by one.
            skip_size += 1

    return numbers
