class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        int count = 0;
        std::sort(nums.begin(), nums.end());
        for (int f = nums.size() - 1; f >= 0; --f) {
            int l = 0;
            int r = f - 1;
            while (l < r) {
                int comb = nums[l] + nums[r];
                if (comb > nums[f]) {
                    count += r - l;
                    r -= 1;
                }
                else {
                    l += 1;
                }
            }
        }
        return count;
    }
};