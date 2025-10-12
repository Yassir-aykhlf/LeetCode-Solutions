class Solution:
    def balancedString(self, s: str) -> int:
        max_len = len(s) // 4
        freq = collections.Counter(s)
        overflow = {num: count-max_len for num, count in freq.items() if count > max_len}
        if not overflow:
            return 0
        # now we hunt for the smallest continuous substring that countains all the elements in the overflow
        # its length will resemble the size of the smallest substring that must be replaced to acheive balance
        window = collections.Counter()
        found, required = 0, len(overflow)
        min_len = float('inf')
        l = 0
        for r, char in enumerate(s):
            window[char] += 1
            if char in overflow and window[char] == overflow[char]:
                found += 1
            while required == found:
                min_len = min(min_len, r - l + 1)
                if s[l] in overflow and window[s[l]] == overflow[s[l]]:
                    found -= 1
                window[s[l]] -= 1
                l += 1
        return min_len