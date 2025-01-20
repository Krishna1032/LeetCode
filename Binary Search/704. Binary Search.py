class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first, last = 0, len(nums) - 1

        while first <= last:
            middle = (first + last) // 2

            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                last = middle - 1
            else:
                first = middle + 1
        return -1
