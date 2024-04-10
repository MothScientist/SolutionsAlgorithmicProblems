func twoSum(nums []int, target int) []int {
    var res []int
    n := len(nums)
    for i := 0; i < n-1; i++ {
        for j := i+1; j < n; j++ {
            if nums[i] + nums[j] == target {
                res = append(res, i, j)
                break
            }
        }
    }
    return res
}