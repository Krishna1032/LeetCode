class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        slow, fast = 0, k - 1
        sums = sum(nums[slow:k])
        max_sum = sums
        while fast < len(nums) - 1:
            slow += 1
            fast += 1
            sums = sums - nums[slow - 1] + nums[fast]
            if sums > max_sum:
                max_sum = sums

        return max_sum / float(k)
