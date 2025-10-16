class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        wsum = 0
        mwsum = float('inf')
        l = 0
        for r in range(len(nums)):
            wsum += nums[r]
            while wsum >= target:
                mwsum = min(mwsum, r - l + 1)
                wsum -= nums[l]
                l += 1
        return mwsum if mwsum != float('inf') else 0