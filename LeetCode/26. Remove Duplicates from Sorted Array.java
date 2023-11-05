class Solution {
    public int removeDuplicates(int[] nums) {
        int j = 1;
        for(short i = 1; i < nums.length; i++){
            if(nums[i] != nums[i-1]){
                nums[j] = nums[i];
                j++;
            }
        }
        return j;
    }
}