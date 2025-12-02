class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine): return False
        vault = list(magazine)
        for c in ransomNote:
            if c not in vault:
                return False
            vault.remove(c)
        return True