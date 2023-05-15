// 11. Container With Most Water

class Solution {
public:
    int maxArea(vector<int>& height) {

        if(height.size() == 2){
            if(height[0] > height[1]){
                return height[1];
            }
            else{
                return height[0];
            }
        }

        int left = 0;
        int right = height.size() - 1;
        int max_area = 0;
        int area = 0;

        while (left < right){

            if (height[right] < height[left]){
                area = (right - left) * height[right];
            }
            else{
                area = (right - left) * height[left];
            }

            if (area > max_area){
                max_area = area;
            }

            if (height[right] < height[left]){ 
                right -= 1;
            }
            else{
                left += 1;
            }
        }
        return max_area;
    }
};