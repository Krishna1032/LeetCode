class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        n = len(s)
        unique = set([])
        longest = 0

        for r in range(n):
            while s[r] in unique:
                unique.remove(s[l])
                l += 1

            unique.add(s[r])
            longest = max(longest, (r - l + 1))

        return longest
