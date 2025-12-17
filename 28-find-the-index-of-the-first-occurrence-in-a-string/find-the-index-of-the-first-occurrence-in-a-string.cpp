class Solution {
public:
    int strStr(string haystack, string needle) {
        // return haystack.find(needle);

        // int n = haystack.size();
        // int m = needle.size();
        // for (int i = 0; i < n - m + 1; ++i) {
        //     if (haystack.substr(i, m) == needle) {
        //         return i;
        //     }
        // }
        // return -1;

        int n = haystack.size();
        int m = needle.size();
        if (m == 0) return 0;
        if (m > n) return -1;
        int base = 26;
        long long mod = 1e9 + 7;
        long long highest_pow = 1;
        for (int i = 0; i < m - 1; ++i) {
            highest_pow = (highest_pow * base) % mod;
        }
        long long n_hash = 0;
        for (int i = 0; i < m; ++i) {
            n_hash = (n_hash * base + needle[i]) % mod;
        }
        long long h_hash = 0;
        for (int i = 0; i < m; ++i) {
            h_hash = (h_hash * base + haystack[i]) % mod;
        }
        if (h_hash == n_hash) {
            return 0;
        }
        for (int i = 1; i < n - m + 1; ++i) {
            h_hash = ((h_hash - haystack[i - 1] * highest_pow % mod + mod) * base + haystack[i + m - 1]) % mod;
            if (h_hash == n_hash) {
                return i;
            }
        }
        return -1;
    }
};