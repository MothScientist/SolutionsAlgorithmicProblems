#include <stdio.h>

int removeElement(int* nums, int numsSize, int val) {
    int res = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] == val) {
            // Shift elements to the left
            for (int j = i; j < numsSize - 1; j++) {
                nums[j] = nums[j + 1];
            }
            nums[numsSize - 1] = -1; // Fill the last element with a placeholder
            res++;
            i--; // Move back one step to recheck the current index after shifting
        }
    }
    return numsSize - res;
}
