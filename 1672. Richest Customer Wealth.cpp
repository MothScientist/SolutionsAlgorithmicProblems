/*
	1672. Richest Customer Wealth
	LeetCode Easy

	Need to return the largest sum of a subarray

	We use the built-in functions of the STL library to sort the list and reverse it, 
	so we can quickly find the largest subarray.

	Example 1:
	Input: accounts = [[1,2,3],[3,2,1]]
	Output: 6

	Example 2:
	Input: accounts = [[1,5],[7,3],[3,5]]
	Output: 10
*/

class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int max_sum = 0;
        int t_max = 0;
        sort (accounts.begin(), accounts.end());
        reverse(accounts.begin(), accounts.end());
        for (int i = 0; i < accounts.size(); i++) 
        {
            t_max += accumulate(accounts[i].begin(), accounts[i].end(), 0);

            if (t_max > max_sum) 
            {
                max_sum = t_max;
            } 
            
            t_max = 0;
        } 
        return max_sum;
    }
};