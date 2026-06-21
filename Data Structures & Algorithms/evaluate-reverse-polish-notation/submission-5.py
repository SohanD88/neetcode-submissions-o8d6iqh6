class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        hmop = {"+", "-", "*", "/"}
        for i in tokens:
            if i not in hmop:
                stk.append(int(i))
            else:
                if i == "+":
                    stk.append(int(stk.pop()) + int(stk.pop()))
                if i == "-":
                    temp = int(stk.pop())
                    stk.append(int(stk.pop()) - temp)
                if i == "*":
                    stk.append(int(stk.pop()) * int(stk.pop()))
                if i == "/":
                    temp = int(stk.pop())
                    stk.append(int((int(stk.pop()) / temp)))
        return stk[-1]



        