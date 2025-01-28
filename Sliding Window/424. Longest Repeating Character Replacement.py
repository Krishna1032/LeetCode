class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        longest = 0
        count = [0] * 26

        for r in range(len(s)):
            count[ord(s[r]) - 65] += 1
            while (r - l + 1) - max(count) > k:
                count[ord(s[l]) - 65] -= 1
                l = l + 1
            longest = max(longest, (r - l + 1))
        return longest
