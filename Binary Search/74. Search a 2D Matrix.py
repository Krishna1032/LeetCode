class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        for nums in matrix:
            left, right = 0, n - 1
            if nums[left] <= target <= nums[right]:
                while left <= right:
                    middle = (left + right) // 2
                    if target == nums[middle]:
                        return True
                    elif target > nums[middle]:
                        left = middle + 1
                    else:
                        right = middle - 1
                return False
        return False
