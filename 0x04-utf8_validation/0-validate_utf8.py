#!/usr/bin/python3
""" A method that determines if a given data
"" set represents a valid UTF-8 encoding """


def validUTF8(data):
    """ Number of bytes in the current UTF-8 character """
    num_bytes = 0
    for n in data:
        byte = format(n, '#010b')[-8:]
        if num_bytes == 0:
            if byte[0] == '1':
                num_bytes = len(byte.split('0')[0])
            if num_bytes > 4 or byte == 1:
                return False
            if num_bytes == 0:
                continue
        else:
            if not (byte[0] == '1' and byte[1] == '0'):
                return False
        num_bytes -= 1
    return num_bytes == 0
