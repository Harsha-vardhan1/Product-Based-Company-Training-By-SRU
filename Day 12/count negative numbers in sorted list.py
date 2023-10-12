class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res=0
        for l in grid:
            for i in l[::-1]:
                if i<0:
                    res+=1
                else:
                    break
        return res
