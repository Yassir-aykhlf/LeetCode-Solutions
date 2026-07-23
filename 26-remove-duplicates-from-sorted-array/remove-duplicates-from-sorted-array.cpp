class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int read = 1;
        int write = 1;
        while (read < nums.size()) {
            if (nums[read] != nums[read - 1]) {
                nums[write] = nums[read];
                write++;
            }
            read += 1;
        }
        return write;
    }
};