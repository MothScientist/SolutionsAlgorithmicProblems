#include <unordered_map>
#include <string>

class Solution {
public:
    int romanToInt(std::string s) {
        std::unordered_map<char, int> math = {
            {'I', 1}, {'V', 5}, {'X', 10},
            {'L', 50}, {'C', 100}, {'D', 500}, {'M', 1000}
        };
        
        int answer = 0;
        int digit = math[s[0]];
        
        for (int i = 1; i < s.length(); i++) {
            if (math[s[i]] == math[s[i - 1]]) {
                digit += math[s[i - 1]];
            } else {
                digit += math[s[i]];
                if (math[s[i]] > math[s[i - 1]]) {
                    answer += 2 * math[s[i]] - digit;
                    digit = 0;
                } else {
                    answer += digit - math[s[i]];
                    digit = math[s[i]];
                }
            }
        }
        
        answer += digit;
        return answer;
    }
};

