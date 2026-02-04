class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        acc_index = {0: -1}
        acc = 0
        max_inter = 0
        for i, n in enumerate(nums):
            acc += 1 if n == 1 else -1
            # target = acc - n
            if acc in acc_index:
                max_inter = max(max_inter, i - acc_index[acc])
            else:
                acc_index[acc] = i
        return max_inter