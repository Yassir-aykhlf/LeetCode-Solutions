class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        double win_sum = std::accumulate(nums.begin(), nums.begin() + k, 0);
        double max_sum = win_sum;
        for (int r = k; r < nums.size(); ++r) {
            win_sum += nums[r];
            win_sum -= nums[r - k];
            max_sum = std::max(max_sum, win_sum);
        }
        return max_sum / k;
    }
};