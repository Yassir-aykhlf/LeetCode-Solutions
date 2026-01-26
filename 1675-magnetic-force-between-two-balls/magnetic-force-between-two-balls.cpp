class Solution {
public:
    bool check(vector<int>& position, int m, int distance) {
        int placed = 1;
        int last_pos = position[0];
        for (int i = 1; i < position.size(); ++i) {
            if (position[i] - last_pos >= distance) {
                placed += 1;
                last_pos = position[i];
                if (placed == m) {
                    return true;
                }
            }
        }
        return placed >= m;
    }
    int maxDistance(vector<int>& position, int m) {
        std::sort(position.begin(), position.end());
        int low = 1, high = position.back(), mid, ans = high;
        while (low <= high) {
            mid = (low + high) / 2;
            if (check(position, m, mid)) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return ans;
    }
};