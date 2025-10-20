class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        vault = collections.Counter(magazine)
        for c in ransomNote:
            vault[c] -= 1
            if vault[c] < 0:
                return False
        return True