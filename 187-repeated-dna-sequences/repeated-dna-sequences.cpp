class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        if (s.size() < 10)
            return {};
        std::unordered_set<std::string> seen;
        std::unordered_set<std::string> res;
        for (int i = 0; i < s.size() - 9; ++i) {
            std::string slice = s.substr(i, 10);
            if (seen.contains(slice) == false) {
                seen.insert(slice);
            }
            else {
                res.insert(slice);
            }
        }
        std::vector<std::string> result(res.begin(), res.end());
        return result;
    }
};