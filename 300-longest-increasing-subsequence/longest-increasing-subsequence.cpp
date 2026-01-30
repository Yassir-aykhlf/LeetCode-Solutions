class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        std::vector<int> LIS;
        for (int n : nums) {
            auto it = std::lower_bound(LIS.begin(), LIS.end(), n);
            if (it == LIS.end())
                LIS.push_back(n);
            else
                LIS[std::distance(LIS.begin(), it)] = n;
        }    
        return LIS.size();
    } 
};