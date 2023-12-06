impl Solution {
    pub fn sort_array(nums: Vec<i32>) -> Vec<i32> {
        if nums.len() < 2 {
            return nums;
        } else if nums.len() == 2 {
            if nums[0] > nums[1] {
                return vec![nums[1], nums[0]];
            } else {
                return nums;
            }
        }
        let mut left = nums[0..nums.len() / 2].to_vec();
        let mut right = nums[nums.len() / 2..].to_vec();
        left = Solution::sort_array(left);
        right = Solution::sort_array(right);
        let (mut li, mut ri, mut i) = (0, 0, 0);
        let mut result = vec![0; nums.len()];
        while li < left.len() && ri < right.len() {
            if left[li] < right[ri] {
                result[i] = left[li];
                li += 1;
            } else if right[ri] < left[li] {
                result[i] = right[ri];
                ri += 1;
            } else {
                result[i] = left[li];
                i += 1;
                result[i] = right[ri];
                li += 1;
                ri += 1;
            }
            i += 1;
        }
        while li < left.len() {
            result[i] = left[li];
            i += 1;
            li += 1;
        }
        while ri < right.len() {
            result[i] = right[ri];
            i += 1;
            ri += 1;
        }
        result.resize(i, 0);
        result
    }
}
