class Solution {
public:
    int fourSumCount(vector<int>& nums1, vector<int>& nums2, vector<int>& nums3, vector<int>& nums4) {
        std::unordered_map<int, int> map;
        for (size_t i = 0; i < nums1.size(); ++i) {
            for (size_t j = 0; j < nums2.size(); ++j) {
                map[nums1[i] + nums2[j]] += 1;
            }
        }
        int count = 0;
        for (size_t i = 0; i < nums3.size(); ++i) {
            for (size_t j = 0; j < nums4.size(); ++j) {
                count += map[-(nums3[i] + nums4[j])];
            }
        }
        return count;
    }
};