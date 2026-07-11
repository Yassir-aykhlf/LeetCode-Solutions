class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = sorted(nums1)
        s2 = sorted(nums2)
        remaining = []
        mapping = defaultdict(list)
        j = 0
        for i in range(len(nums1)):
            if s1[i] > s2[j]:
                mapping[s2[j]].append(s1[i])
                j += 1
            else:
                remaining.append(s1[i])
        res = []
        for num in nums2:
            if mapping[num]:
                res.append(mapping[num].pop())
            else:
                res.append(remaining.pop())
        return res