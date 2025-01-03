class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word_count = [len(word) for word in strs]
        minimum_word = strs[word_count.index(min(word_count))]
        count = 0

        for i in range(len(minimum_word)):
            char = minimum_word[i]
            for words in strs:
                if words[i] == char:
                    continue
                else:
                    return minimum_word[:count]
            count += 1

        prefix = minimum_word[:count]
        return prefix
