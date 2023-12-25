class board:
    def __init__(self, n):
        self.board = [[-1 for _ in range(n)]for _ in range(n)] 
        self.n = n
    
    def isSafe(self, x, y): 
        if(x >= 0 and y >= 0 and x < self.n and y < self.n and self.board[x][y] == -1): 
            return True
        return False
    
    def printSolution(self): 
        for i in range(self.n): 
            for j in range(self.n): 
                print(self.board[i][j],end =' ') 
            print() 
    
    def solveKT(self): 
        move_x = [2, 1, -1, -2, -2, -1, 1, 2] 
        move_y = [1, 2, 2, 1, -1, -2, -2, -1] 
        self.board[0][0] = 0
        pos = 1
      
        if(not self.solveKTUtil(0, 0, move_x, move_y, pos)): 
            print("leave me alone")
        else: 
            self.printSolution()

    def solveKTUtil(self, curr_x, curr_y, move_x, move_y, pos): 
        if(pos == self.n**2): 
            return True
      
        for i in range(8): 
            new_x = curr_x + move_x[i] 
            new_y = curr_y + move_y[i] 
            if(self.isSafe(new_x, new_y)): 
                self.board[new_x][new_y] = pos 
                if(self.solveKTUtil(new_x, new_y, move_x, move_y, pos+1)): 
                    return True
                
                # Backtracking 
                self.board[new_x][new_y] = -1
        return False

#---------- Main ----------#
chessboard = board(5)
chessboard.solveKT()