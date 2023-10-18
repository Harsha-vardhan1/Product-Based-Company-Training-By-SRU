class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        st=[]
        for c in s:
            if(len(st)==0):
                if c!="#":
                 st.append(c)
            elif c=="#":
                st.pop()
            elif c!="#":
                st.append(c)

        res1="".join(st)
        st1=[]
        for c in t:
            if(len(st1)==0):
                if c!="#":
                 st1.append(c)
            elif c=='#':
                st1.pop()
            elif c!="#":
                st1.append(c)
        res2="".join(st1)
        print(res1)
        print(res2)
        if(res1==res2):
            return True
        return False
