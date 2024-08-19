class Solution {
public:
    int minSteps(int n) {
        if (n==1) return 0;
        int out=n;
        for(int i = 1; i<=(n/2); i++){
            for(int j = 1; j<=(n/2); j++){
                if(i*j==n) out= min(out,minSteps(i)+minSteps(j));
            }
        }
        return out;
    }
};