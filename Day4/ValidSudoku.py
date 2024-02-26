class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

      # creating dictionary with hashset for each row,column and 3X3 square
        rows=collections.defaultdict(set)
        cols=collections.defaultdict(set)
        squares=collections.defaultdict(set)

      # iterating and checking if the hashset aldready contains the value or not 
        for r in range(9):
            for c in range(9):
                if(board[r][c]=="."):
                    continue
                if(board[r][c] in rows[r] 
                or board[r][c] in cols[c] or 
                board[r][c] in squares[(r//3,c//3)]):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])

        return True
        
