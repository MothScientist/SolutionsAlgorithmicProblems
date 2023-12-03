class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int high = 0;
        int max_high = high;
        for(int i = 0; i < gain.size(); i++){
            high += gain[i];
            if(high > max_high){
                max_high = high;
            }
        }
        return max_high;
    }
};