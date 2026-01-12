class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        def check(n):
            seen = set()
            base = 101
            mod = 10 ** 9 + 7
            highest_pow = pow(base, n - 1, mod)
            hash1 = 0
            hash2 = 0
            for i in range(n):
                hash1 = (hash1 * base + nums1[i]) % mod
            seen.add(hash1)
            for i in range(n, len(nums1)):
                new = nums1[i]
                old = nums1[i - n]
                hash1 = ((hash1 - old * highest_pow) * base + new) % mod
                seen.add(hash1)
            for i in range(n):
                hash2 = (hash2 * base + nums2[i]) % mod
            if hash2 in seen:
                return True
            for i in range(n, len(nums2)):
                new = nums2[i]
                old = nums2[i - n]
                hash2 = ((hash2 - old * highest_pow) * base + new) % mod
                if hash2 in seen:
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