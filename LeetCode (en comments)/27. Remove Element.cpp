#include <vector>

class Solution {
public:
    int removeElement(std::vector<int>& nums, int val) {
        int res = 0;
        while (std::find(nums.begin(), nums.end(), val) != nums.end()) {
            nums.erase(std::find(nums.begin(), nums.end(), val));
            nums.push_back('_');
            res++;
        }
        return nums.size() - res;
    }
};
