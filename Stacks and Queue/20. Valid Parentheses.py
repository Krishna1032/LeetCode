class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {")": "(", "}": "{", "]": "["}

        for bracket in s:
            if bracket in brackets.values():
                stack.append(bracket)
            else:
                if stack:
                    if stack[-1] != brackets[bracket]:
                        return False
                    else:
                        stack.pop()
                else:
                    return False

        return not stack
