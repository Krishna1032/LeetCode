from typing import List


class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n = len(temp)
        result = [0] * n
        stack = []

        for i in range(n):
            while stack and temp[i] > temp[stack[-1]]:
                index = stack.pop()
                result[index] = i - index
            stack.append(i)
        return result


if __name__ == "__main__":
    solution = Solution()
    x = solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
    print(x)
