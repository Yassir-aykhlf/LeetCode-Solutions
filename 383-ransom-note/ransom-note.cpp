class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        if (ransomNote.size() > magazine.size()) {
            return false;
        }
        std::unordered_map<char, int> vault;
        for (char c : magazine) {
            vault[c] += 1;
        }
        for (char c : ransomNote) {
            vault[c] -= 1;
            if (vault[c] < 0) {
                return false;
            }
        }
        return true;
    }
};