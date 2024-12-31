class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        max_length = max(len(word1), len(word2))
        joined = []
        for i in range(max_length):
            if i < len(word1):
                joined.append(word1[i])
            if i < len(word2):
                joined.append(word2[i])

        return "".join(joined)
