class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 0, num
        while left <= right:
            middle = (left + right) // 2
            value = middle**2
            if value == num:
                return True
            elif value > num:
                right = middle - 1
            else:
                left = middle + 1
        return False
