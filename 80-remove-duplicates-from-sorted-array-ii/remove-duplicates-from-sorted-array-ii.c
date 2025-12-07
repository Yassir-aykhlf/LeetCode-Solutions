int removeDuplicates(int* nums, int numsSize) {
    if (numsSize <= 2)
        return numsSize;
    int r = 2;
    for (int i = 2; i < numsSize; ++i) {
        if (nums[i] != nums[r - 2]) {
            nums[r] = nums[i];
            r += 1;
        }
    }
    return r;
}