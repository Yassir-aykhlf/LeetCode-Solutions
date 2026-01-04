class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        std::stack<std::pair<int, int>> stk;
        int max_area = 0;
        int n = heights.size();
        for (int i = 0; i < n; ++i) {
            int start = i;
            while (!stk.empty() && stk.top().second > heights[i]) {
                std::pair<int, int> top = stk.top(); stk.pop();
                int index = top.first;
                int h = top.second;
                max_area = max(max_area, h * (i - index));
                start = index;
            }
            stk.push({start, heights[i]});
        }
        while (!stk.empty()) {
            pair<int, int> top = stk.top(); stk.pop();
            max_area = max(max_area, top.second * (n - top.first));
        }
        return max_area;
    }
};