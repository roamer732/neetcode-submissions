class MinStack:

    def __init__(self):
        self.st = []
        self.mst = []
        
    def push(self, val: int) -> None:
        self.st.append(val)       
        if not self.mst or self.mst[-1] >= val:
            self.mst.append(val)
        
    def pop(self) -> None:
        if self.st[-1] == self.mst[-1]:
            self.mst.pop()
        self.st.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.mst[-1]
        
