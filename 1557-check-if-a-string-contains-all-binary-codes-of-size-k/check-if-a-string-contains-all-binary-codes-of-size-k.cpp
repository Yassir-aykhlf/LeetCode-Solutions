class Solution {
public:
    bool hasAllCodes(string s, int k) {
        if (s.size() < k)
            return false;
        std::unordered_set<std::string> seen;
        for (int i = 0; i < s.size() - k + 1; ++i)
            seen.insert(s.substr(i, k));
        return seen.size() == (1 << k);
    }
};