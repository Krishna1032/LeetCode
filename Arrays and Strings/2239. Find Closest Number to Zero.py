class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        abs_nums = [abs(x) for x in nums]
        min_value = min(abs_nums)
        if min_value in nums:
            return min_value
        else:
            return -min_value
