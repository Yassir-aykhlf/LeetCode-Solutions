class Solution {
public:
    int minPairSum(vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        int l = 0;
        int r = nums.size() - 1;
        int max_sum = INT_MIN;
        while (l < r) {
            int sum = nums[l] + nums[r];
            max_sum = std::max(max_sum, sum);
            l += 1;
            r -= 1;
        }
        return max_sum;
    }
};