// 35. Search Insert Position
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        if (nums[0] > target){
            return 0;
        }
        if (nums[nums.size() - 1] == target){
            return nums.size() - 1;
        }
        if (nums[nums.size() - 1] < target){
            return nums.size();
        }
        for (int i = 0; i < nums.size() - 1; i++){
            if (nums[i] < target and nums[i+1] > target){
                return i+1;
            }
            else if (nums[i] == target){
                return i;
            }
        }
        return 0;
    }
};