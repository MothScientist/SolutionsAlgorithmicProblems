#include <unordered_map>
#include <string>

class Solution {
public:
    int romanToInt(std::string s) {
        std::unordered_map<char, int> d = {
            {'I', 1}, {'V', 5}, {'X', 10},
            {'L', 50}, {'C', 100}, {'D', 500}, {'M', 1000}
        };
        int res = 0;
        int diff = d[s[0]];
        for (int i = 1; i < s.length(); i++) {
           if (d[s[i]] == d[s[i - 1]]){
                diff += d[s[i]];
           }
           else if (d[s[i]] > d[s[i - 1]]){
               res += d[s[i]] - diff;
               diff = 0;
           }
           else if (d[s[i]] < d[s[i - 1]]){
               res += diff;
               diff = d[s[i]];
           }
        }
        res += diff;
        return res;
    }
};

