class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        chars = list(pattern)
        words = s.split()
        if len(chars) != len(words):
            return False
        char_word = {}
        word_char = {}
        for c, w in zip(chars, words):
            if c in char_word and char_word[c] != w or \
               w in word_char and word_char[w] != c:
               return False
            char_word[c] = w
            word_char[w] = c
        return True