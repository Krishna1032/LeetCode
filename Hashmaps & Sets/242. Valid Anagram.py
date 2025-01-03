class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_char = {}

        for char in s:
            if char in s_char:
                s_char[char] += 1
            else:
                s_char[char] = 1

        for char in t:
            if char in s_char:
                s_char[char] -= 1
            else:
                return False

        for key, value in s_char.items():
            if value != 0:
                return False
        return True
