class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        int n = matrix.size();
        int low = matrix[0][0];
        int high = matrix[n - 1][n - 1];
        int ans = high;
        while (low <= high) {
            int mid = (low + high) / 2;
            int count = 0;
            int row = 0, col = n - 1;
            while (row < n && col >= 0) {
                if (matrix[row][col] <= mid) {
                    count += (col + 1);
                    row += 1;
                }
                else {
                    col -= 1;
                }
            }
            if (count >= k) {
                ans = mid;
                high = mid - 1;
            }
            else {
                low = mid + 1;
            }
        }
        return ans;
    }
};