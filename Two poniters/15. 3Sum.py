class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        i = 0
        l = i + 1
        r = len(nums) - 1

        answer = []

        for i in range(len(nums) - 1):
            target = -nums[i]
            l = 0
            r = len(nums) - 1
            while l < r:
                if l == i:
                    l += 1
                    continue
                if r == i:
                    r -= 1
                    continue
                value = nums[l] + nums[r]
                print((l, r))
                print(value)
                if value == target:
                    ans = sorted([nums[i], nums[l], nums[r]])
                    if ans not in answer:
                        answer.append(ans)
                    break
                elif value < 0:
                    l += 1
                else:
                    r -= 1

        return answer
