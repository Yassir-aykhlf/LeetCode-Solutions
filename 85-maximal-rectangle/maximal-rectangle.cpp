class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int n = heights.size();
        std::stack<std::pair<int, int>> stk;
        int max_area = 0;
        for (int i = 0; i < n; ++i) {
            int start = i;
            while (!stk.empty() && stk.top().second > heights[i]) {
                pair<int, int> p = stk.top(); stk.pop();
                int index = p.first;
                int h = p.second;
                max_area = max(max_area, h * (i - index));
                start = index;
            }
            stk.push({start, heights[i]});
        }
        while (!stk.empty()) {
            pair<int, int> p = stk.top(); stk.pop();
            int i = p.first;
            int h = p.second;
            max_area = max(max_area, h * (n - i));
        }
        return max_area;
    }
    int maximalRectangle(vector<vector<char>>& matrix) {
        if (matrix.empty() || matrix[0].empty()) {
            return 0;
        }
        int max_area = 0;
        int m = matrix.size();
        int n = matrix[0].size();
        std::vector<int> cols(n, 0);
        for (int row = 0; row < m; ++row) {
            for (int col = 0; col < n; ++col) {
                if (matrix[row][col] == '1') {
                    cols[col] += 1;
                }
                else {
                    cols[col] = 0;
                }
            }
            max_area = max(max_area, largestRectangleArea(cols));
        }
        return max_area;
    }
};