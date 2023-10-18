class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st=[]
        #print(int("58")+int("42"))
        for s in operations:
            if len(st)>0 and s=="C":
                st.pop()
            elif s=="D":
                st.append(2*st[-1])
            elif s=="+":
                st.append(st[-1]+st[-2])
            else:
                st.append(int(s))

        return sum(st)