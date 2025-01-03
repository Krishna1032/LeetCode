class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_indices = {}
        for i, value in enumerate(nums):
            if value in nums_indices:
                nums_indices[value].append(i)
            else:
                nums_indices[value] = [i]

        for key, value in nums_indices.items():
            complement = target - int(key)
            index = value.pop(-1)
            if complement in nums_indices and nums_indices[complement] != []:
                return [index, nums_indices[complement][-1]]
