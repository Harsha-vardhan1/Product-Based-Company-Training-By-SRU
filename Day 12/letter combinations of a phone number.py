class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d={'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        '''if(len(digits)==0):
            return []
        elif(len(digits)==1):
            res=[]
            for c in d[digits[0]]:
                res.append(c)
            return res
        elif(len(digits)==2):
            res=[]
            for c in d[digits[0]]:
                for a in d[digits[1]]:
                    res.append(c+a)
            return res
        elif(len(digits)==3):
            res=[]
            for a in d[digits[0]]:
                for b  in d[digits[1]]:
                    for c in d[digits[2]]:
                        res.append(a+b+c)
            return res
        elif(len(digits)==4):
            res=[]
            for a in d[digits[0]]:
                for b  in d[digits[1]]:
                    for c in d[digits[2]]:
                        for e in d[digits[3]]:
                         res.append(a+b+c+e)
            return res'''
        '''if len(digits)==0:
            return []
        elif(len(digits)==1):
            res=[]
            def combinations1(i):
                res.append(d[digits[0]][i])
                if(i<2):
                    combinations1(i+1)
            combinations1(0)
            return res
        elif(len(digits)==2):
            res=[]
            def combinations1(i,j):
                res.append(d[digits[0]][i]+d[digits[1]][j])
                if(i<2):
                    combinations1(i+1,j+1)
            combinations1(0,0)
            return res'''
        res=[]
        def backtrack(i,curstr):
            if(len(digits)==len(curstr)):
                res.append(curstr)
                return
            for c in d[digits[i]]:
                backtrack(i+1,curstr+c)
        if digits:
                backtrack(0,"")
        return res
            

        
        

        
        
        
       
