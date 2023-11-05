// 198. House Robber
class Solution {
public:
    int rob(vector<int>& nums) {
        if(nums.size() == 1){
            return nums[0];
        }
        if(nums.size() == 2){
            if(nums[0] > nums[1]){
                return nums[0];
            }
            return nums[1];
        }
        int dp[nums.size()];
        for(int i = 0; i < nums.size(); i++){
            dp[i] = 0;
        }
        dp[0] = nums[0];
        if(nums[0] > nums[1]){
            dp[1] = nums[0];
        }
        else{
            dp[1] = nums[1];
        }
        for(int i = 2; i < nums.size(); i++){
            if(dp[i-1] > dp[i-2] + nums[i]){
                dp[i] = dp[i-1];
            }
            else{
                dp[i] = dp[i-2] + nums[i];
            }
        }
        return dp[nums.size() - 1];
    }
};