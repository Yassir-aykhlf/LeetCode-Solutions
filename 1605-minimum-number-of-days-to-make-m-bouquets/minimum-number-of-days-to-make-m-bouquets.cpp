class Solution {
public:
    bool    check(vector<int>& bloomDay, int m, int k, int day) {
        int flowers = 0, bouquets = 0;
        for (auto b : bloomDay) {
            if (b <= day) {
                flowers += 1;
                if (flowers == k) {
                    bouquets += 1;
                    flowers = 0;
                }
            }
            else {
                flowers = 0;
            }
        }
        return bouquets >= m;
    }
    int     minDays(vector<int>& bloomDay, int m, int k) {
        int res = -1;
        int low = *std::min_element(bloomDay.begin(), bloomDay.end());
        int high = *std::max_element(bloomDay.begin(), bloomDay.end());
        int mid; 
        while (low <= high) {
            mid = low + (high - low) / 2;
            if (check(bloomDay, m, k, mid)) {
                res = mid;
                high = mid - 1;
            }
            else {
                low = mid + 1;
            }
        }
        return res;
    }
};