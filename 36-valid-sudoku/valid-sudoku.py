class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            rowlis = []
            collis = []
            row = set()
            col = set()
            for j in range(9):
                if (board[j][i] != "."):
                    col.add(board[j][i])
                    collis.append(board[j][i])
                if (board[i][j] != "."):
                    row.add(board[i][j])
                    rowlis.append(board[i][j])
            
            if len(row) != len(rowlis) or len(col) != len(collis):
                return False
        
        for i in range(9):
            box = set()
            boxlis = []
            for j in range(3):
                for k in range(3):
                    if (board[(i%3)*3+j][(i//3)*3+k] != "."):
                        box.add(board[(i%3)*3+j][(i//3)*3+k])
                        boxlis.append(board[(i%3)*3+j][(i//3)*3+k])
            if (len(box) != len(boxlis)):
                return False
            




        return True