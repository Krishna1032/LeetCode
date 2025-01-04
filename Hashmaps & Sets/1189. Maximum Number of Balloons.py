class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count_char = {}
        for char in text:
            if char in count_char:
                count_char[char] += 1
            else:
                count_char[char] = 1

        balloon = {"b": 1, "a": 1, "l": 2, "o": 2, "n": 1}
        smallest_count = float("inf")
        for key, value in balloon.items():
            if key in count_char:
                times = count_char[key] // value
                if times < smallest_count:
                    smallest_count = times
            else:
                return 0

        return smallest_count
