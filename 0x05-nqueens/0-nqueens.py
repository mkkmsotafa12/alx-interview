#!/usr/bin/python3
""" N Queens problem solver """

import ctypes
import sys


class NQueensSolver:
    """
    Class to solve the N Queens problem using a shared C library """

    def __init__(self, size: int):
        """
        Initialize the NQueensSolver with the given board size.

        Args:
            size (int): The size of the board (number of queens).
        """
        self.size = size
        self.lib = ctypes.CDLL("./libnqueens.so")

    def solve(self):
        """ Solve the N Queens problem using the shared C library """
        self.lib.solve_nqueens(self.size)


def main():
    """ Main function to handle command line arguments and start the solver """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solver = NQueensSolver(n)
    solver.solve()


if __name__ == "__main__":
    main()
