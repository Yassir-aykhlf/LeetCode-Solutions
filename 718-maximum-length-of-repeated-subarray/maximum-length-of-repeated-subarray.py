class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        def check(length):
            if length == 0:
                return True

            seen = set()
            BASE = 101
            MOD = 10**9 + 7
            highest_pow = pow(BASE, length - 1, MOD)

            h1 = 0
            for i in range(length):
                h1 = (h1 * BASE + nums1[i]) % MOD
            seen.add(h1)
            for i in range(1, len(nums1) - length + 1):
                h1 = (h1 - nums1[i - 1] * highest_pow) % MOD
                h1 = (h1 * BASE + nums1[i + length - 1]) % MOD
                seen.add(h1)

            h2 = 0
            for i in range(length):
                h2 = (h2 * BASE + nums2[i]) % MOD
            if h2 in seen:
                return True
            for i in range(1, len(nums2) - length + 1):
                h2 = (h2 - nums2[i - 1] * highest_pow) % MOD
                h2 = (h2 * BASE + nums2[i + length - 1]) % MOD
                if h2 in seen:
                    return True
                    
            return False

        low, high = 0, min(len(nums1), len(nums2))
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans  = mid
                low  = mid + 1
            else:
                high = mid - 1
        return ans