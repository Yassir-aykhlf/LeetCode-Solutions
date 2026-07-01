class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        chars = list(pattern)
        words = s.split()
        if len(chars) != len(words):
            return False
        char_to_word = {}
        word_to_char = {}
        for char, word in zip(chars, words):
            if char in char_to_word and char_to_word[char] != word or \
                word in word_to_char and word_to_char[word] != char:
                return False
            char_to_word[char] = word
            word_to_char[word] = char
        return True