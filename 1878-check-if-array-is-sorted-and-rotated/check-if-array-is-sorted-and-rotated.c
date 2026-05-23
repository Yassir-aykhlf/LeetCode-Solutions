bool check(int* nums, int numsSize) {
    size_t count = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] > nums[(i + 1) % numsSize]) {
            if (count > 0) {
                return false;
            }
            count++;
        }
    }
    return true;
}