class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums_ = set()
        res = []
        for n in nums:
            if n in nums_:
                res.append(n)
            else:
                nums_.add(n)
        return res