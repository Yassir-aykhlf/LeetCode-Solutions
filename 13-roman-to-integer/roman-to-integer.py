class Solution:
    def romanToInt(self, s: str) -> int:
        roman_int = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        res = roman_int[s[-1]]
        for i in range(len(s) - 1):
            if roman_int[s[i]] < roman_int[s[i + 1]]:
                res -= roman_int[s[i]]
            else:
                res += roman_int[s[i]]
        return res