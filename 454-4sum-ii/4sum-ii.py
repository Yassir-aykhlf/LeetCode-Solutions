""" 
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                for k in range(len(nums3)):
                    for l in range(len(nums4)):
                        if not nums1[i] + nums2[j] + nums3[k] + nums4[l]:
                            count += 1
        return count
"""
    # how can I optimize this?
""" 
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count = 0
        _nums4_counts = Counter(nums4)
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                for k in range(len(nums3)):
                    target = -(nums1[i] + nums2[j] + nums3[k])
                    count += _nums4_counts[target]
        return count
"""
    # still not enough, how can optimize further?
""" 
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        precalc_nums1_x_nums2 = defaultdict(int)
        precalc_nums3_x_nums4 = defaultdict(int)
        for i in range(len(nums1)):
            for j in range(i, len(nums2)):
                precalc_nums1_x_nums2[nums1[i] + nums2[j]] += 1
        for i in range(len(nums3)):
            for j in range(i, len(nums4)):
                precalc_nums3_x_nums4[nums3[i] + nums4[j]] += 1
        count = 0
        for sum1 in precalc_nums1_x_nums2.keys():
            count += precalc_nums3_x_nums4[-sum1]
        return count
"""
    # did not work

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hashma = defaultdict(int)
        for i in range(len(nums3)):
            for j in range(len(nums4)):
                hashma[nums3[i] + nums4[j]] += 1
        count = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                count += hashma[-(nums1[i] + nums2[j])]
        return count