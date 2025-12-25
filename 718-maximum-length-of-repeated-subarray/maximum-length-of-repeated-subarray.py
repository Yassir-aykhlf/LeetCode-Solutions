class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        def check(n):
            hash1, hash2 = 0, 0
            base, mod = 101, 10**9 + 7
            highest_pow = pow(base, n - 1, mod)
            seen = set()
            # calc hash of the first window of nums1
            for i in range(n):
                hash1 = (hash1 * base + nums1[i]) % mod
            seen.add(hash1)
            # calc the hashs of the rest of nums1
            for i in range(1, len(nums1) - n + 1):
                new = nums1[i + n - 1]
                old = (nums1[i - 1] * highest_pow) % mod
                hash1 = ((hash1 - old) * base + new) % mod
                seen.add(hash1)
            # calc hash of the first window of nums2
            for i in range(n):
                hash2 = (hash2 * base + nums2[i]) % mod
            if hash2 in seen:
                return True
            for i in range(1, len(nums2) - n + 1):
                new = nums2[i + n - 1]
                old = (nums2[i - 1] * highest_pow) % mod
                hash2 = ((hash2 - old) * base + new) % mod
                if hash2 in seen:
                    return True
            return False

        l, r = 0, min(len(nums1), len(nums2))
        ans = 0
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans