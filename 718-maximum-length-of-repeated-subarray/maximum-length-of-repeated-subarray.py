class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        def check(n):
            base, mod = 101, 10 ** 9 + 7
            highest_pow = pow(base, n - 1, mod)
            h1, h2 = 0, 0
            seen = set()
            for i in range(n):
                h1 = (h1 * base + nums1[i]) % mod
            seen.add(h1)
            for i in range(n, len(nums1)):
                new = nums1[i]
                old = nums1[i - n]
                h1 = ((h1 - old * highest_pow) * base + new) % mod
                seen.add(h1)
            
            for i in range(n):
                h2 = (h2 * base + nums2[i]) % mod
            if h2 in seen:
                return True
            for i in range(n, len(nums2)):
                new = nums2[i]
                old = nums2[i - n]
                h2 = ((h2 - old * highest_pow) * base + new) % mod
                if h2 in seen:
                    return True
            return False

        lo, hi = 0, min(len(nums1), len(nums2))
        ans = 0
        while lo <= hi:
            n = (lo + hi) // 2
            if check(n):
                ans = n
                lo = n + 1
            else:
                hi = n - 1
        return ans