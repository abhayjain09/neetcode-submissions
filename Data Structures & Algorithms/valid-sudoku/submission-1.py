from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            dic = {}
            for j in range(9):
                if board[i][j] in dic and board[i][j] != ".": 
                    return False
                dic[board[i][j]] = True
        for i in range(9):
            dic = {}
            for j in range(9):
                if board[j][i] in dic and board[j][i] != ".": 
                    return False
                dic[board[j][i]] = True

        for row_start in range(0, 9, 3):
            for col_start in range(0, 9, 3):
                dic = {}
                for j in range(row_start, row_start + 3):
                    for k in range(col_start, col_start + 3):
                        if board[j][k] in dic and board[j][k] != ".": 
                            return False
                        dic[board[j][k]] = True


        return True