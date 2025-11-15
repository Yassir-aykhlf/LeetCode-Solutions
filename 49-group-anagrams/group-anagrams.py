class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for str_ in strs:
            key = ''.join(sorted(str_))
            group[key].append(str_)
        return [lst for lst in group.values()]