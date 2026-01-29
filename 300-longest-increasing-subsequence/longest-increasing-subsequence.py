class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        seq = []
        for n in nums:
            if not seq or n > seq[-1]:
                seq.append(n)
            else:
                lo, hi = 0, len(seq) - 1
                while lo < hi:
                    mid = (lo + hi) // 2
                    if seq[mid] >= n:
                        hi = mid
                    else:
                        lo = mid + 1
                seq[hi] = n
        return len(seq)