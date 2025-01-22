class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        if nums[left] < nums[right]:
            return nums[left]

        while nums[left] > nums[right]:
            middle = (left + right) // 2
            if nums[middle] > nums[left]:
                left = middle
            elif nums[middle] < nums[left]:
                right = middle
            else:
                return nums[right]
        return nums[left]
