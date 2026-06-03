void gameOfLife(int** board, int boardSize, int* boardColSize) {
    int m = boardSize, n = *boardColSize;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            int live = 0;
            for (int y = i - 1; y <= i + 1; y++) {
                for (int x = j - 1; x <= j + 1; x++) {
                    if (y >= 0 && y < m && x >= 0 && x < n && !(y == i && x == j)) {
                        if (board[y][x] == 1 || board[y][x] == 2) {
                            live += 1;
                        }
                    }
                }
            }
            if (board[i][j] == 1 && (live < 2 || live > 3)) {
                board[i][j] = 2;
            }
            if (board[i][j] == 0 && (live == 3)) {
                board[i][j] = 3;
            }
        }
    }
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (board[i][j] == 2) {
                board[i][j] = 0;
            }
            else if (board[i][j] == 3) {
                board[i][j] = 1;
            }
        }
    }
}