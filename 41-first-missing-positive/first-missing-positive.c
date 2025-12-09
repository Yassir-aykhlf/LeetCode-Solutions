int firstMissingPositive(int* nums, int numsSize) {
    int n = numsSize;
    for (int i = 0; i < n; ++i) {
        if (nums[i] < 1 || nums[i] > n) {
            nums[i] = n + 1;
        }
    }
    for (int i = 0; i < n; ++i) {
        int index = abs(nums[i]) - 1;
        if (index >= 0 && index < n) {
            if (nums[index] > 0) {
                nums[index] *= -1;
            }
        }
    }
    for (int i = 0; i < n; ++i) {
        if (nums[i] > 0) {
            return i + 1;
        }
    }
    return n + 1;
}