class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window = nums[:k]
        wsum = sum(window)
        mwsum = wsum
        n = len(nums)
        for r in range(k, n):
            wsum += nums[r]
            wsum -= nums[r - k]
            mwsum = max(mwsum, wsum)
        return mwsum / k