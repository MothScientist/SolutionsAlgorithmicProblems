class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        else if (x < 10) {
            return true;
        }

        string str = to_string(x);

        for (string::size_type i = 0; i < str.size(); i++)
        {
            if (str[i] != str[str.size() - 1 - i])
            {
                return false;
            }
        }

        return true;
    }
};