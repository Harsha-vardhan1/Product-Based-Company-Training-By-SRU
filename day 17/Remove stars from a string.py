class Solution:
    def removeStars(self, s: str) -> str:
        st=[]
        for c in s:
            if(len(st)==0):
                st.append(c)
            elif(c=="*"):
                st.pop()
            else:
                st.append(c)
        return "".join(st)
        