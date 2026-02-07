class Solution:
    """ Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order. """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.Counter(nums)
        return heapq.nlargest(k, freq.keys(), key=lambda x: freq[x])