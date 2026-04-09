class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # set up hashsets
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                # If blank then skip
                if board[r][c] == ".":
                    continue
                # Check for if duplicate in row, col, or subsquare
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or 
                    board[r][c] in squares[(r//3, c//3)]):
                    return False
                
                # Add the numbers into the hashsets
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[r//3, c//3].add(board[r][c])
        return True
