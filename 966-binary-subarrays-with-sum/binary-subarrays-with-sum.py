class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atMostK(k):
            if k < 0:
                return 0
            curr = 0
            count = 0
            l = 0
            for r in range(len(nums)):
                curr += nums[r]
                while curr > k:
                    curr -= nums[l]
                    l += 1
                count += r - l + 1
            return count
        return atMostK(goal) - atMostK(goal - 1)