class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        def check(n):
            seen = set()
            MOD = 10 ** 9 + 7
            BASE = 101
            highest_pow = pow(BASE, n - 1, MOD)
            hash1 = 0
            for i in range(n):
                hash1 = (hash1 * BASE + nums1[i]) % MOD
            seen.add(hash1)
            for i in range(n, len(nums1)):
                new = nums1[i]
                old = nums1[i - n]
                hash1 = ((hash1 - old * highest_pow) * BASE + new) % MOD
                seen.add(hash1)
            hash2 = 0
            for i in range(n):
                hash2 = (hash2 * BASE + nums2[i]) % MOD
            if hash2 in seen:
                return True
            for i in range(n, len(nums2)):
                new = nums2[i]
                old = nums2[i - n]
                hash2 = ((hash2 - old * highest_pow) * BASE + new) % MOD
                if hash2 in seen:
                    return True
            return False
        lo, hi = 0, min(len(nums1), len(nums2))
        ans = hi
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans