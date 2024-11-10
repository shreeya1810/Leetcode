class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<int> v(n,1);            
        for(int i=m-2;i>=0;i--){
            for(int j=n-2;j>=0;j--){
                    v[j]=v[j+1]+v[j];
            }
            
        }
        return v[0];
    }
};