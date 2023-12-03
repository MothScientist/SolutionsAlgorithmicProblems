#include <string>
#include <algorithm>

class Solution {
public:
    int lengthOfLongestSubstring(std::string s) {
        std::string subString;
        int maxLength = 0;

        for (char c : s) {
            auto it = std::find(subString.begin(), subString.end(), c);
            if (it != subString.end()) {
                subString.erase(subString.begin(), it + 1);
            }
            subString.push_back(c);
            maxLength = std::max(maxLength, static_cast<int>(subString.length()));
        }

        return maxLength;
    }
};