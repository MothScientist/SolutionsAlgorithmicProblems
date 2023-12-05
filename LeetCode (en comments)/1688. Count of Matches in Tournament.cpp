class Solution {
public:
    int numberOfMatches(int n) {
        // To determine the winner, n-1 participants must be eliminated
        return n - 1;
    }
};