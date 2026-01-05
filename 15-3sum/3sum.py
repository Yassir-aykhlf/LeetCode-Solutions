class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            a = i + 1
            b = n - 1
            while a < b:
                comb = nums[i] + nums[a] + nums[b]
                if comb == 0:
                    res.append([nums[i], nums[a], nums[b]])
                    while a < b and nums[a] == nums[a + 1]:
                        a += 1
                    while a < b and nums[b] == nums[b - 1]:
                        b -= 1
                    a += 1
                    b -= 1
                elif comb < 0:
                    a += 1
                else: 
                    b -= 1
        return res