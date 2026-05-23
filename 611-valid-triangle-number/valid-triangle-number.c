int compare(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}
int triangleNumber(int* nums, int numsSize) {
    qsort(nums, numsSize, sizeof(int), compare);
    int count = 0;
    for (int i = numsSize - 1; i >= 2; i--) {
        int l = 0;
        int r = i - 1;
        while (l < r) {
            if (nums[l] + nums[r] > nums[i]) {
                count += (r - l);
                r--;
            }
            else {
                l++;
            }
        }
    }
    return count;
}