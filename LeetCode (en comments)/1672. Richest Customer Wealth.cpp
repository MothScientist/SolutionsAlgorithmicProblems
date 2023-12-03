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