#!/usr/bin/python3
""" A method that determines if a given data
"" set represents a valid UTF-8 encoding """


def validUTF8(data):
    """ Number of bytes in the current UTF-8 character """
    num_bytes = 0
    mask1 = 1 << 7  # 10000000 in binary
    mask2 = 1 << 6  # 01000000 in binary

    for n in data:
        if num_bytes == 0:
            mask = 1 << 7
            while mask & n:
                num_bytes += 1
                mask >>= 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (n & mask1 and not (n & mask2)):
                return False

        num_bytes -= 1

    return num_bytes == 0
