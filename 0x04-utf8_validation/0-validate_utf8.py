#!/usr/bin/ python3
""" A method that determines if a given data set represents a valid UTF-8 encoding """


def validUTF8(data):
    """ Number of bytes in the current UTF-8 character """
    num_bytes = 0
    
    """ Masks to identify the number of bytes in a character """
    masks = [
        0b10000000,  # 1 byte character (0xxxxxxx)
        0b11100000,  # 2 byte character (110xxxxx 10xxxxxx)
        0b11110000,  # 3 byte character (1110xxxx 10xxxxxx 10xxxxxx)
        0b11111000   # 4 byte character (11110xxx 10xxxxxx 10xxxxxx 10xxxxxx)
    ]
    
    """ Masks for checking the continuation bytes (must start with 10xxxxxx) """
    continuation_mask = 0b11000000
    continuation_bits = 0b10000000
    
    for byte in data:
        byte = byte & 0xFF
        
        if num_bytes == 0:
            """ Determine the number of bytes in this UTF-8 character """
            if (byte & masks[0]) == 0:
                num_bytes = 1
            elif (byte & masks[1]) == 0b11000000:
                num_bytes = 2
            elif (byte & masks[2]) == 0b11100000:
                num_bytes = 3
            elif (byte & masks[3]) == 0b11110000:
                num_bytes = 4
            else:
                return False
        else:
            """ Check for continuation bytes (must start with 10) """
            if (byte & continuation_mask) != continuation_bits:
                return False
        
        """ Decrease the number of bytes to process for the current character """
        num_bytes -= 1
    
    """ If we end up with num_bytes not being zero, the UTF-8 encoding is incomplete """
    return num_bytes == 0
