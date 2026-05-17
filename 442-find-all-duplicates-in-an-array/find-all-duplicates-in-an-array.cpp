class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        int n = nums.size();
        vector<int> mask(n + 1, 0);
        vector<int> res;
        for (int i = 0; i < n; ++i) {
            if (mask[nums[i]]) {
                res.push_back(nums[i]);
                continue;
            }
            mask[nums[i]] = -1;
        }
        return res;
    }
};