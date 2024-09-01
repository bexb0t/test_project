# https://leetcode.com/problems/valid-sudoku/

"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""

from typing import Any, List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check for 9 rows 9 cols
        # 9 rows
        if len(board) != 9:
            return False
        # 9 cols
        if any([len(row) != 9 for row in board]):
            return False
        # actually lets transform the list to get cols.
        cols = [list(row) for row in zip(*board)]

        # rows and cols
        for i in range(0, 9):
            if not self.is_valid_group(board[i]):
                print(f"Row {i} not valid.")
                return False
            if not self.is_valid_group(cols[i]):
                print(f"Col {i} not valid.")
                return False

        # subsquares: 0, 1, 2 - 3, 4, 5 -  6, 7, 8
        # row 0,1,2, cols 0, 1, 2
        # row 0, 1,2, cols 3, 4, 5
        # row 0, 1, 2, cols 6, 7, 8
        # row 3, 4, 5, cols 0,1,2
        # row 3, 4, 5, cosl 3, 4, 5
        for offset in range(0, 7, 3):
            group = []
            for row in range(0, 3):
                x = offset + row
                for col in range(0, 3):
                    y = offset + col
                    val = board[x][y]
                    group.append(val)
            if not self.is_valid_group(group):
                print("Invalid values in square.")
                return False
        return True

    def is_valid_group(self, group: List[Any]):
        # remove .
        group = [n for n in group if n.strip() != "."]
        # contains 1-9
        if not all([n.isnumeric() and 0 < int(n) < 10 for n in group]):
            return False
        # no repeats
        return len(set(group)) == len(group)


if __name__ == "__main__":
    solution = Solution()

    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    print(f"result: {solution.isValidSudoku(board)}, expected: true")

    board = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    print(f"result: {solution.isValidSudoku(board)}, expected: false")
