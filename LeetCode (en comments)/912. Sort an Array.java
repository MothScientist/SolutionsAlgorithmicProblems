class Solution {
    public int[] sortArray(int[] nums) {
        if (nums.length < 2) {
            return nums;
        } else if (nums.length == 2) {
            if (nums[0] > nums[1]) {
                return new int[]{nums[1], nums[0]};
            } else {
                return nums;
            }
        }
        int[] left = Arrays.copyOfRange(nums, 0, nums.length / 2);
        int[] right = Arrays.copyOfRange(nums, nums.length / 2, nums.length);
        left = sortArray(left);
        right = sortArray(right);
        int li = 0, ri = 0, i = 0;
        int[] result = new int[nums.length];
        while (li < left.length && ri < right.length) {
            if (left[li] < right[ri]) {
                result[i] = left[li];
                li++;
            } else if (right[ri] < left[li]) {
                result[i] = right[ri];
                ri++;
            } else {
                result[i] = left[li];
                i++;
                result[i] = right[ri];
                li++;
                ri++;
            }
            i++;
        }
        while (li < left.length) {
            result[i] = left[li];
            i++;
            li++;
        }
        while (ri < right.length) {
            result[i] = right[ri];
            i++;
            ri++;
        }
        return Arrays.copyOf(result, i);
    }
}
