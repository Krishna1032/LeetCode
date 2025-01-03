class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        char_hash = {}
        for char in stones:
            if char in char_hash:
                char_hash[char] += 1
            else:
                char_hash[char] = 1

        sum = 0
        for char in jewels:
            if char in stones:
                sum += char_hash[char]
        return sum
