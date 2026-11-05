class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        Notations = { "+", "-","*", "/"}

        for c in tokens:
            if c not in Notations:
                stack.append(int(c))
                continue

            a = stack.pop()
            b = stack.pop()

            if c == "+":
                stack.append(a + b)
            elif c == "-":
                stack.append(b - a)
            elif c == "/":
                stack.append( int(float(b) / a))
            
            elif c == "*":
                stack.append(a * b)
        return stack[-1]