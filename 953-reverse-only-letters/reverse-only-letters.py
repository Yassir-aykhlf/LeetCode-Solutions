class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l, r = 0, len(s) - 1
        s_ = list(s)
        while l < r:
            if not s_[l].isalpha():
                l += 1
                continue
            if not s_[r].isalpha():
                r -= 1
                continue
            s_[l], s_[r] = s_[r], s_[l]
            l += 1
            r -= 1
        return ''.join(s_)