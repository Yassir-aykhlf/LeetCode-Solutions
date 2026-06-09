class Solution:
    def romanToInt(self, s: str) -> int:
        syms = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        translate = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        acc = translate[s[-1]]
        for i in range(len(s) - 2, -1, -1):
            sym = s[i]
            if syms.index(s[i]) < syms.index(s[i + 1]):
                acc -= translate[sym]
            else:
                acc += translate[sym]
        return acc