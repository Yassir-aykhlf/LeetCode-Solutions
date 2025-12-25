class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atMostK(k):
            if k < 0: return 0
            cur = 0
            count = 0
            l = 0
            for r in range(len(nums)):
                cur += nums[r]
                while cur > k:
                    cur -= nums[l]
                    l += 1
                count += r - l + 1
            return count
        return atMostK(goal) - atMostK(goal - 1)