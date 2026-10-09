class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) 
    {
        unordered_set<char>rows[9];
        unordered_set<char>cols[9];
        unordered_set<char>grids[9];

        for(int i=0;i<9;i++)
        {
            for(int j=0;j<9;j++)
            {
                char val = board[i][j];
                if(val == '.')
                    continue;
                
                int grid = (i/3)*3 + (j/3);
                if(rows[i].find(val) != rows[i].end())
                    return false;
                if(cols[j].find(val) != cols[j].end())
                    return false;
                if(grids[grid].find(val) != grids[grid].end())
                    return false;
                
                rows[i].insert(val);
                cols[j].insert(val);
                grids[grid].insert(val);
            }
        }
        return true;
    }
};