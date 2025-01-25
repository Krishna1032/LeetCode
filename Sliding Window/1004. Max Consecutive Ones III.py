class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        longest = 0
        zeros = 0

        while right < len(nums):
            longest += 1
            if nums[right] == 0:
                zeros += 1
            if zeros > k:
                zeros -= 1 - nums[left]
                left = left + 1
                longest = right - left + 1
            right += 1
        return longest
