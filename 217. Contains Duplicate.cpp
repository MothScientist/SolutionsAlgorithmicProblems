// 217. Contains Duplicate
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        std::sort(std::begin(nums), std::end(nums));
        for (int i = 0; i < nums.size() - 1; i++){
            if (nums[i] == nums[i+1]){
                return true;
            }
        }
        return false;
    }
};