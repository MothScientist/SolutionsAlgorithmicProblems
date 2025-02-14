// 1
func missingNumber(nums []int) int {
    nums_len := len(nums)

    correct_nums_sum := (nums_len*(nums_len+1))/2
    sum_nums := 0

    for i := 0; i < nums_len; i++ {
        sum_nums += nums[i]
    }

    return correct_nums_sum - sum_nums
}

// 2
func missingNumber(nums []int) int {
    nums_len := len(nums)

    correct_nums_sum := 0
    sum_nums := 0

    for i := 0; i < nums_len; i++ {
        correct_nums_sum += i
        sum_nums += nums[i]
    }

    correct_nums_sum += nums_len

    return correct_nums_sum - sum_nums
}