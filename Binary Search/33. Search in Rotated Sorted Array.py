class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif nums[right] < target < nums[left]:
                return -1
            elif (
                nums[left] <= target < nums[middle]
                or target >= nums[left] > nums[middle]
                or target < nums[middle] < nums[right]
            ):
                right = middle - 1
            else:
                left = middle + 1
        return -1
