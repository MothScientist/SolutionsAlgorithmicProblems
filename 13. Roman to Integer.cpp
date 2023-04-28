#include <iostream>
#include <string>
#include <map>

int roman_to_int(std::string &str) {
    std::map<char, int> roman = {
        {'I', 1},
        {'V', 5},
        {'X', 10},
        {'L', 50},
        {'C', 100},
        {'D', 500},
        {'M', 1000}
    };
    int digit = roman[str[0]];
    int answer = 0;
    for (int i = 1; i < str.size(); i++) {
        if (str[i] == str[i - 1]) {
            digit += roman[str[i - 1]];
        }
        else {
            digit += roman[str[i]];
            if (roman[str[i]] > roman[str[i - 1]]) {
                answer += 2 * roman[str[i]] - digit;
                digit = 0;
            }
            else {
                answer += digit - roman[str[i]];
                digit = roman[str[i]];
            }
        }
    }

    answer += digit;

    return answer;
}

int main() {
    std::string digit;
    std::cin >> digit;
    std::cout << roman_to_int(digit);

    std::cout << "\n";
    return 0;
}
