class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def isIsomorphic(word):
            if len(word) != len(pattern):
                return False
            word_pattern = {}
            pattern_word = {}
            for w, p in zip(word, pattern):
                if w in word_pattern and word_pattern[w] != p:
                    return False
                if p in pattern_word and pattern_word[p] != w:
                    return False
                word_pattern[w] = p
                pattern_word[p] = w
            return True
        return [word for word in words if isIsomorphic(word)]