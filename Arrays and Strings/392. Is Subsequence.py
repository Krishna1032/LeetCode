class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False

        for char in s:
            if char in t:
                t = t[t.index(char) + 1 :]
            else:
                return False
        return True
