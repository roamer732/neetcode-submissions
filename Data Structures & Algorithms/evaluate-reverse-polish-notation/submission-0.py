class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for i in tokens:
            if i not in ["+", "-", "*", "/"]:
                st.append(int(i))
                continue
            
            n1 = st.pop()
            n2 = st.pop()
            if i == "+":
                st.append(n1+n2)
            elif i == "-":
                st.append(n2-n1)
            elif i == "*":
                st.append(n1*n2)
            else:
                st.append(int(n2/n1))
        return st[0]
        