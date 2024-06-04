#!/usr/bin/python3


"""
Problem: You have n number of locked boxes in front of you.
         Each box is numbered sequentially from 0 to n - 1
         and each box may contain keys to the other boxes.
Task: Write a method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Check if all boxes can be opened.

    Parameters:
    boxes (list of list of int): The boxes with their keys.

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """
    if type(boxes) is not list:
        return False
    elif (len(boxes)) == 0:
        return False
    for i in range(1, len(boxes) - 1):
        boxes_checked = False
        for y in range(len(boxes)):
            boxes_checked = i in boxes[y] and i != y
            if boxes_checked:
                break
        if boxes_checked is False:
            return boxes_checked
    return True
