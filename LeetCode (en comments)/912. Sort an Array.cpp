class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        if (nums.size() < 2) {
            return nums;
        } else if (nums.size() == 2) {
            if (nums[0] > nums[1]) {
                return {nums[1], nums[0]};
            } else {
                return nums;
            }
        }
        vector<int> left(nums.begin(), nums.begin() + nums.size() / 2);
        vector<int> right(nums.begin() + nums.size() / 2, nums.end());
        left = sortArray(left);
        right = sortArray(right);
        int li = 0, ri = 0;
        vector<int> result;
        while (li < left.size() && ri < right.size()) {
            if (left[li] < right[ri]) {
                result.push_back(left[li]);
                li++;
            } else if (right[ri] < left[li]) {
                result.push_back(right[ri]);
                ri++;
            } else {
                result.push_back(left[li]);
                result.push_back(right[ri]);
                li++;
                ri++;
            }
        }
        while (li < left.size()) {
            result.push_back(left[li]);
            li++;
        }
        while (ri < right.size()) {
            result.push_back(right[ri]);
            ri++;
        }
        return result;
    }
};