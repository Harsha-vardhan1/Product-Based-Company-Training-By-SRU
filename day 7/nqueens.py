n=int(input())
def solveNQueens(n: int):
        res = []
        col = []
        pos = []
        neg = []
        board = [['.']*(n) for i in range(n)]
        def back(r):
            if r==n:
                l = ["".join(i) for i in board]
                res.append(l)
                return
            for c in range(n):
                if c in col or (r+c) in pos or (r-c) in neg:
                    continue
                board[r][c] = 'Q'
                col.append(c)
                pos.append(r+c)
                neg.append(r-c)
                back(r+1)
                board[r][c]='.'
                col.remove(c)
                pos.remove(r+c)
                neg.remove(r-c)
            return res
        print(back(0))
print(solveNQueens(0))
