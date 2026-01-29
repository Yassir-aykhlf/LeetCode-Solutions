class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        seq = []
        for n in nums:
            if not seq or n > seq[-1]:
                seq.append(n)
            else:
                idx = bisect.bisect_left(seq, n)
                seq[idx] = n
        return len(seq)