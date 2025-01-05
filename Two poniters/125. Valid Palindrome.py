class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        stripped = re.sub(r"[^a-z0-9]", "", s)

        if stripped != stripped[::-1]:
            return False

        return True
