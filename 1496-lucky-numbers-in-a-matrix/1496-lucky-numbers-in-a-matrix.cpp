#include <set>

class Solution {
public:
    vector<int> luckyNumbers (vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        vector <int> out;
        set<int> rows, cols;
        for(int i=0;i<m;i++){
            if(!(rows.find(i) != rows.end())){
                for(int j=0; j<n;j++){
                    if(!(cols.find(j) != cols.end())){
                        bool acceptable = 1;
                        for(int k = 0;k<m;k++){
                            if(matrix[k][j]>matrix[i][j]){
                                acceptable = 0;
                                break;
                            }
                        }
                        if(acceptable){
                            for(int k = 0;k<n;k++){
                                if(matrix[i][k]<matrix[i][j]){
                                    acceptable = 0;
                                    break;
                                }
                            }
                        }
                        if(acceptable){
                            out.push_back(matrix[i][j]);
                            rows.insert(i);
                            cols.insert(j);
                        }
                    }
                }
            }
        }
        return out;
    }
};