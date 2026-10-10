class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        d = defaultdict(int)
        count = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                d[nums1[i] + nums2[j]] += 1
        for i in range(len(nums3)):
            for j in range(len(nums4)):
                count += d[-(nums3[i] + nums4[j])]
        return count