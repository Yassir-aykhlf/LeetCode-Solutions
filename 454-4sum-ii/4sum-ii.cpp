class Solution {
public:
    int fourSumCount(vector<int>& nums1, vector<int>& nums2, vector<int>& nums3, vector<int>& nums4) {
        std::unordered_map<int, int> map;
        int count = 0;
        for (int num1 : nums1) {
            for (int num2 : nums2) {
                map[num1 + num2] += 1; 
            }
        }
        for (int num3 : nums3) {
            for (int num4: nums4) {
                count += map[-(num3 + num4)];
            }
        }
        return count;
    }
};