class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if not board:
            return 0
        result=0
        row=len(board)
        col=len(board[0])
        for i in range(row):
            for j in range(col):
                if (i==0 or board[i-1][j]=='.') and (j==0 or board[i][j-1]=='.') and board[i][j]=='X':
                    result+=1
        return result
