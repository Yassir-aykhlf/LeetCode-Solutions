class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        res = 0
        while i <= j:
            if i == j:
                res += nums[i]
                break
            com = int(str(nums[i]) + str(nums[j]))
            res += com
            i += 1
            j -= 1
        return res