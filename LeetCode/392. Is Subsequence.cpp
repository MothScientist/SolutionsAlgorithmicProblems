// 392. Is Subsequence
class Solution {
public:
    bool isSubsequence(string s, string t) {
        int pointer_s = 0;
        if (s.size() == 0){
            return true;
        }
        for (int pointer_t = 0; pointer_t < t.size(); pointer_t++){
            if (s[pointer_s] == t[pointer_t]){
                pointer_s += 1;
                if (pointer_s == s.size()){
                    return true;
                }
            }
        }
        return false;
    }
};