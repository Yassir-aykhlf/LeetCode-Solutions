class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        hmap = Counter(nums)
        count = 0
        for num in hmap.keys():
            if k > 0:
                if num + k in hmap:
                    count += 1
            if k == 0:
                if hmap[num] > 1:
                    count += 1
        return count