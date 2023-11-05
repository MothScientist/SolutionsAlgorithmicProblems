int finalValueAfterOperations(vector<string>& operations) {
    int res = 0;
    for (int i = 0; i < operations.size(); i++){
        for (int j = 0; j < operations[i].size(); j++){
            if (operations[i][j] == '+'){
                res++;
                break;
            }
            if (operations[i][j] == '-'){
                res--;
                break;
            }
        }
    }
    return res;
}