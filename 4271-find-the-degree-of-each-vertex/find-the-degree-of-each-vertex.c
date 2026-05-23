/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findDegrees(int** matrix, int matrixSize, int* matrixColSize, int* returnSize) {
    int *result = malloc(sizeof(int) * matrixSize);
    for (int i = 0; i < matrixSize; i++) {
        int count = 0;
        for (int j = 0; j < matrixSize; j++) {
            if (matrix[i][j]) {
                count++;
            }
        }
        result[i] = count;
    }
    *returnSize = matrixSize;
    return result;
}