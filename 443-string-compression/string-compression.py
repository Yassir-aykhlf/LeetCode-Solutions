class Solution:
    def compress(self, chars: list[str]) -> int:
        n = len(chars)
        w = 0
        i = 0
        while i < len(chars):
            char = chars[i]
            j = i
            while j < len(chars) and chars[j] == char:
                j += 1
            count = j - i
            i = j
            chars[w] = char
            w += 1
            if count > 1:
                for c in str(count):
                    chars[w] = c
                    w += 1
        return w