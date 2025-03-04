class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if target == nums[middle]:
                return middle

            elif target < nums[middle]:
                right = middle - 1

            else:
                left = middle + 1

        return left
