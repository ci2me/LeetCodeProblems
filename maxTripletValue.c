long long maximumTripletValue(int* nums, int numsSize) {
    if (numsSize < 3) return 0;

    // create arrays
    long long int left_max[numsSize];
    long long int right_max[numsSize];

    // When parsing through the array for j, this array
    // will show the corresponding highest value to the left
    // of index j
    left_max[0] = nums[0];
    for (int i = 1; i < numsSize; i++) {
        left_max[i] = (nums[i] > left_max[i - 1]) ? nums[i] : left_max[i - 1];
    }

    // Build right_max array
    // When parsing through the array for j, this array
    // will show the corresponding highest value to the right
    // of index j
    right_max[numsSize - 1] = nums[numsSize - 1];
    for (int i = numsSize - 2; i >= 0; i--) {
        right_max[i] = (nums[i] > right_max[i + 1]) ? nums[i] : right_max[i + 1];
    }

    long long ans = 0;

    // Compute the maximum triplet value
    for (int i = 1; i < numsSize - 1; i++) {
        long long left = left_max[i - 1];
        long long right = right_max[i + 1];
        long long temp_ans = (left - nums[i]) * right;

        // if current answer is greater than saved answer, update saved
        ans = (temp_ans > ans) ? temp_ans : ans;
    }

    return ans;
}
