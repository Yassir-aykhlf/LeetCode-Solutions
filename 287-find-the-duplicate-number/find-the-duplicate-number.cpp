class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int a = 0;
        int b = 0;
        while (true) {
            a = nums[a];
            b = nums[nums[b]];
            if (a == b) {
                break;
            }
        }
        a = 0;
        while (nums[a] != nums[b]) {
            a = nums[a];
            b = nums[b];
        }
        return nums[a];
    }
};