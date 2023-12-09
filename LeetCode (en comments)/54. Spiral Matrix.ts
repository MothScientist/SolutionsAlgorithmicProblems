function spiralOrder(matrix: number[][]): number[] {
    const result: number[] = [];
    let top: number = 0;
    let bottom: number = matrix.length - 1;
    let left: number = 0;
    let right: number = matrix[0].length - 1;

    while (result.length < matrix.length * matrix[0].length) {
        for (let i = left; i <= right; i++) {
            result.push(matrix[top][i]);
        }
        top++;

        for (let i = top; i <= bottom; i++) {
            result.push(matrix[i][right]);
        }
        right--;

        if (top <= bottom) {
            for (let i = right; i >= left; i--) {
                result.push(matrix[bottom][i]);
            }
            bottom--;
        }

        if (left <= right) {
            for (let i = bottom; i >= top; i--) {
                result.push(matrix[i][left]);
            }
            left++;
        }
    }

    return result;
}