#include <iostream>
#include <string>

class Solution {
public:
    std::string largestGoodInteger(std::string num) {
        num += " ";
        char p1 = ' ';
        int counter = 0;
        std::string res = "";

        for (char i : num) {
            if (counter == 3) {
                if (p1 > res[0]) {
                    res = std::string(1, p1);
                }
            }

            if (i != p1) {
                p1 = i;
                counter = 1;
            } else {
                counter += 1;
            }
        }

        if (!res.empty()) {
            return std::string(3, res[0]);
        } else {
            return "";
        }
    }
};
