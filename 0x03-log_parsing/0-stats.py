#!/usr/bin/python3
""" A script that reads stdin line by line and computes metrics """

import sys


i = 0
sum_file_size = 0
status_codes = {'200': 0,
                '301': 0,
                '400': 0,
                '401': 0,
                '403': 0,
                '404': 0,
                '405': 0,
                '500': 0}

try:
    for line in sys.stdin:
        args: list[str] = line.split(' ')
        if len(args) > 2:
            status_line: str = args[-2]
            file_size: str = args[-1]
            if status_line in status_codes:
                status_codes[status_line] += 1
            sum_file_size += int(file_size)
            i += 1
            if i == 10:
                print('File size: {:d}'.format(sum_file_size))
                sorted_keys: list[str] = sorted(status_codes.keys())
                for key in sorted_keys:
                    value = status_codes[key]
                    if value != 0:
                        print('{}: {}'.format(key, value))
                i = 0
except Exception:
    pass
finally:
    print('File size: {:d}'.format(sum_file_size))
    sorted_keys = sorted(status_codes.keys())
    for key in sorted_keys:
        value: int = status_codes[key]
        if value != 0:
            print('{}: {}'.format(key, value))
