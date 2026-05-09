class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def genKey(string: str) -> str:
            chars = [0] * 26
            for c in string:
                chars[ord(c) - ord('a')] += 1
            res = ""
            for i, c in enumerate(chars):
                if c > 0:
                    res += f'{c}{chr(i + ord('a'))}'
            return res
        anagrams = {}
        for str in strs:
            key = genKey(str)
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(str)
        return list(anagrams.values())