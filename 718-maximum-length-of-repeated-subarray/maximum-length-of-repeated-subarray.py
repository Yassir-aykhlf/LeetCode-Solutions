class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        def check(n):
            seen = set()
            mod = 10 ** 9 + 7
            base = 101
            highest_pow = pow(base, n - 1, mod)
            h1_hash, h2_hash = 0, 0
            for i in range(n):
                h1_hash = (h1_hash * base + nums1[i]) % mod
            seen.add(h1_hash)
            for i in range(n, len(nums1)):
                new = nums1[i]
                old = nums1[i - n]
                h1_hash = ((h1_hash - old * highest_pow) * base + new) % mod
                seen.add(h1_hash)
            
            for i in range(n):
                h2_hash = (h2_hash * base + nums2[i]) % mod
            if h2_hash in seen:
                return True
            for i in range(n, len(nums2)):
                new = nums2[i]
                old = nums2[i - n]
                h2_hash = ((h2_hash - old * highest_pow) * base + new) % mod
                if h2_hash in seen:
                    return True
            return False
        lo, hi = 0, min(len(nums1), len(nums2))
        while lo <= hi:
            n = (lo + hi) // 2
            if check(n):
                lo = n + 1
            else:
                hi = n - 1
        return hi