func smallestRangeI(nums []int, k int) int {
    min_element, max_element := nums[0], nums[0]

    for _, n := range nums{
        if n < min_element {
            min_element = n
        }
        if n > max_element {
            max_element = n
        }
    }

    res := (max_element - k) - (min_element + k)

    if res > 0 {
        return res
    } else {
        return 0
    }
    
}