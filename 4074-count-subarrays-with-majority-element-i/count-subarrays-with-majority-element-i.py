class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + (nums[i - 1] == target)
        count = 0
        for l in range(n+1):
            for r in range(l+1,n+1):
                if (prefix[r] - prefix[l]) * 2 > (r - l):
                    count += 1
        return count