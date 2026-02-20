class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def isMatch(word: str) -> bool:
            word_list = list(word)
            pattern_list = list(pattern)
            if len(word_list) != len(pattern_list):
                return False
            w_map = {}
            p_map = {}
            for w, p in zip(word_list, pattern_list):
                if w in w_map and w_map[w] != p or \
                   p in p_map and p_map[p] != w:
                   return False
                w_map[w] = p
                p_map[p] = w
            return True
        return [word for word in words if isMatch(word)]