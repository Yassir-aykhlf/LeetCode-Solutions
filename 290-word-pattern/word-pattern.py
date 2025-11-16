class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        chars = list(pattern)
        if len(chars) != len(words):
            return False
        char_word = {}
        word_char = {}
        for char, word in zip(chars, words):
            if char in char_word and char_word[char] != word:
                return False
            if word in word_char and word_char[word] != char:
                return False
            char_word[char] = word
            word_char[word] = char
        return True