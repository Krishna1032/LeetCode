class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        solution = []

        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                solution.append(nums[l] ** 2)
                l += 1
            else:
                solution.append(nums[r] ** 2)
                r -= 1

        solution.reverse()
        return solution
