class Solution {
public:
    bool hasAllCodes(string s, int k) {
        try {
            std::set<std::string> seen;
            for (int i = 0; i < s.size() - k + 1; ++i)
                seen.insert(s.substr(i, k));
            return seen.size() == std::pow(2, k);
        } catch (std::exception &e) {
            std::cout << "You done fucked up! " << e.what();
        }
        return false;
    }
};