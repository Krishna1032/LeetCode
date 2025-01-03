class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        before = [1] * n
        after = [1] * n
        product = 1
        for i in range(len(nums) - 1):
            product *= nums[i]
            before[i + 1] = product

        product = 1
        for i in range(len(nums) - 1, 0, -1):
            product *= nums[i]
            after[i - 1] = product

        solution = [before[i] * after[i] for i in range(n)]
        return solution
