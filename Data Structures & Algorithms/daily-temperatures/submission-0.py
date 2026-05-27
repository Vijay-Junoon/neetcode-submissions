class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = [0]

        for i in range(1,len(temperatures)):
            while stack != [] and temperatures[i] > temperatures[stack[-1]]:
                x = stack.pop()
                ans[x] = i - x
            stack.append(i)
        return ans