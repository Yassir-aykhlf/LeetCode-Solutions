class Solution:
    def makeFancyString(self, s: str) -> str:
        res = []
        i = char_ = count_ = 0
        while i < len(s):
            char_ = s[i]
            count_ = 1
            while i < len(s) and s[i] == char_:
                if count_ < 3:
                    res.append(char_)
                count_ += 1
                i += 1
        return ''.join(res)