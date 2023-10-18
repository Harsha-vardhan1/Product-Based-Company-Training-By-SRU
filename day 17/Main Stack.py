class MinStack:

    def __init__(self):
        self.st=[]

    def push(self, val: int) -> None:
        self.st.append(val)
      
    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        m=self.st[0]
        for i in self.st:
            if(i<m):
                m=i
        return (m)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()