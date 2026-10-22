class Solution:
    def compress(self, chars: list[str]) -> int:
        r, w = 0, 0
        n = len(chars)
        while r < n:
            char = chars[r]
            j = r
            while j < n and chars[j] == chars[r]:
                j += 1
            count = j-r
            r = j
            chars[w] = char
            w += 1
            if count > 1:
                for c in str(count):
                    chars[w] = c
                    w += 1
        return w