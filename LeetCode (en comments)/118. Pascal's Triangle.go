// 1
func generate(numRows int) [][]int {
    pascalTriangle := [][]int{
        {1},
    }
    if numRows == 1 {
        return pascalTriangle
    }
    for i := 0; i < numRows - 1; i++ {
        abc := []int{}
        abc = append(abc, 1)
        for j := 1; j < len(pascalTriangle[i]); j++ {
            abc = append(abc, pascalTriangle[i][j] + pascalTriangle[i][j-1])
        }
        abc = append(abc, 1)
        pascalTriangle = append(pascalTriangle, abc)
    }
    return pascalTriangle
}

// 2
func generate(numRows int) [][]int {
    pascalTriangle := [][]int{
        {1},
    }
    if numRows == 1 {
        return pascalTriangle
    }
    for i := 0; i < numRows - 1; i++ {
        abc := []int{}
        for j := 0; j < len(pascalTriangle[i]); j++ {
            if j == 0 {
                abc = append(abc, pascalTriangle[i][j])
            } else {
                abc = append(abc, pascalTriangle[i][j] + pascalTriangle[i][j-1])
            }
            if j == len(pascalTriangle) - 1{
                abc = append(abc, pascalTriangle[i][j])
            }
        }
        pascalTriangle = append(pascalTriangle, abc)
    }
    return pascalTriangle
}