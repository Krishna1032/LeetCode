from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "*", "/"]
        stack = []

        for token in tokens:
            if token in operators:
                value1 = stack.pop()
                value2 = stack.pop()
                if token == "+":
                    result = value2 + value1
                elif token == "-":
                    result = value2 - value1
                elif token == "*":
                    result = value1 * value2
                else:
                    result = int(value2 / value1)
                stack.append(result)
            else:
                stack.append(int(token))

        return stack[0]


if __name__ == "__main__":
    solution = Solution()
    x = solution.evalRPN(
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    )
    print(x)
