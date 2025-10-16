class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        result  = []
        target = 0
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            a = i + 1
            b = n - 1
            while a < b:
                res = nums[i] + nums[a] + nums[b]
                if res == target:
                    result.append([nums[i], nums[a], nums[b]])
                    while a < b and nums[a] == nums[a + 1]:
                        a += 1
                    while a < b and nums[b] == nums[b - 1]:
                        b -= 1
                    a += 1
                    b -= 1
                elif res < target:
                    a += 1
                else:
                    b -= 1
        return result 