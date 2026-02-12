class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # match numbers to achieve k
        # hashmap for fast lookup
        # 0 k edge case
        freq = Counter(nums)
        count = 0
        for num in freq.keys():
            if k == 0:
                if num in freq and freq[num] > 1:
                    count += 1
            else:
                if num + k in freq:
                    count += 1
        return count