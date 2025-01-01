class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if nums == []:
            return nums
        solution = []
        start = nums[0]
        for i in range(len(nums) - 1):
            if nums[i] + 1 != nums[i + 1]:
                end = nums[i]
                solution.append(f"{start}->{end}" if end != start else f"{start}")
                start = nums[i + 1]
        end = nums[-1]
        solution.append(f"{start}->{end}" if end != start else f"{start}")
        return solution
