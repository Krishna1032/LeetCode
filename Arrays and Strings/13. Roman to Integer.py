class Solution:
    def romanToInt(self, s: str) -> int:
        representation = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        values = [int(representation[symbol]) for symbol in s]
        sum = 0
        for i, value in enumerate(values):
            if value >= values[(i + 1) if i < len(values) - 1 else i]:
                sum += value
            else:
                sum -= value
        return sum
