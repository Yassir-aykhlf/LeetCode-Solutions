class Solution:
    def genKey(self, str_: str) -> str:
        alpha = [0] * 26
        key = ""
        for c in str_:
            alpha[ord(c) - ord('a')] += 1
        for i, c in enumerate(alpha):
            if c > 0:
                key += f"{c}{chr(i + ord('a'))}"
        return key
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for str_ in strs:
            key = self.genKey(str_)
            if key not in groups:
                groups[key] = []
            groups[key].append(str_)
        return [group for group in groups.values()]