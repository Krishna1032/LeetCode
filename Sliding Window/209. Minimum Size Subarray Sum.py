class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        shortest = float("inf")
        sums = 0

        for r in range(len(nums)):
            sums += nums[r]
            while sums >= target:
                shortest = min(shortest, r - l + 1)
                sums -= nums[l]
                l = l + 1

        return shortest if shortest != float("inf") else 0
