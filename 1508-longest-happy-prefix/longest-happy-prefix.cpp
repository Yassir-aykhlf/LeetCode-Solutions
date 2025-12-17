class Solution {
public:
    string longestPrefix(string s) {
        int base = 31;
        int longest_len = 0;
        long long mod = 10e9 + 7;
        long long power = 1;
        long long pre_hash = 0;
        long long suf_hash = 0;
        for (int i = 0; i < s.size() - 1; ++i) {
            pre_hash = (pre_hash * base + s[i]) % mod;
            suf_hash = (suf_hash + s[s.size() - i - 1] * power) % mod;
            power = (power * base) % mod;
            if (pre_hash == suf_hash) {
                longest_len = i + 1;
            }
        }
        return s.substr(0, longest_len);
    }
};