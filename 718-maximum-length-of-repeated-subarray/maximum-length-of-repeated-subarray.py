class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        def search(n):
            base = 101
            mod = 10 ** 9 + 7
            highest_pow = pow(base, n - 1, mod)
            seen = set()
            nums1_hash = 0
            nums2_hash = 0
            for i in range(n):
                nums1_hash = (nums1_hash * base + nums1[i]) % mod
            seen.add(nums1_hash)
            for i in range(n, len(nums1)):
                nums1_hash = ((nums1_hash - nums1[i - n] * highest_pow) * base + nums1[i]) % mod
                seen.add(nums1_hash)
            for i in range(n):
                nums2_hash = (nums2_hash * base + nums2[i]) % mod
            if nums2_hash in seen:
                return True
            for i in range(n, len(nums2)):
                nums2_hash = ((nums2_hash - nums2[i - n] * highest_pow) * base + nums2[i]) % mod
                if nums2_hash in seen:
                    return True
            return False
        lo, hi = 0, min(len(nums1), len(nums2))
        while lo <= hi:
            mid = (lo + hi) // 2
            if search(mid):
                lo = mid + 1
            else:
                hi = mid - 1
        return hi