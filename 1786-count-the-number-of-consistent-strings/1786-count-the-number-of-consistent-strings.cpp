class Solution {
public:
    int countConsistentStrings(string allowed, vector<string>& words) {
        int out = 0;
        bool bol = true;
        
        for (string word : words) {
            bol = true;
            
            for (char a : word) {
                if (allowed.find(a) == string::npos) {
                    bol = false;
                    break;
                }
            }
            
            if (bol) {
                out++;
            }
        }
        
        return out;
    }
};
