class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                a = j + 1
                b = n - 1
                while a < b:
                    comb = nums[i] + nums[j] + nums[a] + nums[b]
                    if comb == target:
                        result.append([nums[i], nums[j], nums[a], nums[b]])
                        while a < b and nums[a] == nums[a + 1]:
                            a += 1
                        while a < b and nums[b] == nums[b - 1]:
                            b -= 1
                        a += 1
                        b -= 1
                    elif comb < target:
                        a += 1
                    else:
                        b -= 1
        return result