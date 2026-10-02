class Solution {
public:
    long long minEnd(int n, int x) {
        long long res = x;
        for (int i = n - 1; i > 0; i--) {
            res = (res + 1) | x;
        }
        return res;
    }
};