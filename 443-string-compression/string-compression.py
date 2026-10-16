class Solution:
    def compress(self, chars: list[str]) -> int:
        w, r = 0, 0
        while r < len(chars):
            j = r
            while j < len(chars) and chars[j] == chars[r]:
                j += 1
            count = j - r
            chars[w] = chars[r]
            w += 1
            r = j
            if count > 1:
                for c in str(count):
                    chars[w] = c
                    w += 1
        return w