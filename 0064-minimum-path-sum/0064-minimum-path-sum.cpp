class Solution {
public:
    int helper(vector<vector<int>>& grid,int n,int m,vector<vector<int>>& memo){
        if(n<0 || m<0)
            return INT_MAX;
        if(m==0&& n==0)
            return grid[0][0];
        if(memo[n][m]!=-1)
            return memo[n][m];
        memo[n][m]=min(helper(grid,n-1,m,memo),helper(grid,n,m-1,memo))+grid[n][m];
        return memo[n][m];
        
    }
    int minPathSum(vector<vector<int>>& grid) {
        vector<vector<int>>memo(grid.size(),vector<int>(grid[0].size(),-1));
        return helper(grid,grid.size()-1,grid[0].size()-1,memo);
        
    }
};