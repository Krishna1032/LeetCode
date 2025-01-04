class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 3
        box_hash = {}
        for i in range(len(board)):
            row_hash = {}
            column_hash = {}

            for j in range(len(board[0])):
                if board[i][j] != ".":
                    if board[i][j] in row_hash:
                        return False
                    else:
                        row_hash[board[i][j]] = "present"

                if board[j][i] != ".":
                    if board[j][i] in column_hash:
                        return False
                    else:
                        column_hash[board[j][i]] = "present"
                if board[i][j] != ".":
                    value = (i // n) * n + (j // n) + 1
                    if board[i][j] in box_hash:
                        box_hash[board[i][j]].append(value)
                    else:
                        box_hash[board[i][j]] = [value]

        for key, values in box_hash.items():
            unique = set(values)
            if len(unique) != len(values):
                return False

        return True
