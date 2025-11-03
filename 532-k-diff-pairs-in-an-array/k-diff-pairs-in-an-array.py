class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        freq = collections.Counter(nums)
        count = 0
        for num in freq.keys():
            if k > 0:
                if num + k in freq:
                    count += 1
            else:
                if freq[num] > 1:
                    count += 1
        return count