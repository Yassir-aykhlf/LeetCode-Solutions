class Solution {
public:
    void sortColors(vector<int>& nums) {
        int low, mid = 0;
        int high = nums.size() - 1;
        while (mid <= high) {
            if (nums[mid] == 0) {
                nums[mid] = nums[low];
                nums[low] = 0;
                low += 1;
                mid += 1;
            }
            else if (nums[mid] == 1) {
                mid += 1;
            }
            else {;
                nums[mid] = nums[high];
                nums[high] = 2;
                high -= 1;
            }
        }
    }
};