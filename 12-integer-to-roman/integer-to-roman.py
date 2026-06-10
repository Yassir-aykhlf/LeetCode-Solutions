class Solution:
    def intToRoman(self, num: int) -> str:
        int_roman = [
            (1000, "M" ),
            (900 , "CM"),
            (500 , "D" ),
            (400 , "CD"),
            (100 , "C" ),
            (90  , "XC"),
            (50  , "L" ),
            (40  , "XL"),
            (10  , "X" ),
            (9   , "IX"),
            (5   , "V" ),
            (4   , "IV"),
            (1   , "I" )
        ]
        res = []
        for val, sym in int_roman:
            if num >= val:
                count = num // val
                res.append(sym * count)
                num %= val
        return "".join(res)