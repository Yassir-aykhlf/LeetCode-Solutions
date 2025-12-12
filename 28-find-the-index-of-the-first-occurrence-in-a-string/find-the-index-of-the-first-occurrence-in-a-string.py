class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = -1
        needle_l = len(needle)
        haystack_l = len(haystack)
        target = list(needle)
        window = list(haystack[:needle_l])
        if window == target:
            return 0
        l = 0
        for r in range(needle_l, haystack_l):
            window.append(haystack[r])
            window.pop(0)
            if window == target:
                return l + 1 
            l += 1
        return -1