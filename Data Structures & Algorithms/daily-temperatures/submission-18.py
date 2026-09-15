class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tempStack = [0] * len(temperatures)

        stack = [] # pair of temp its index 

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                stackTemp, stackIndex = stack.pop()

                tempStack[stackIndex] = i - stackIndex
            stack.append((t,i))

        return tempStack