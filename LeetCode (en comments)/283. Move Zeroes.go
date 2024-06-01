func moveZeroes(nums []int)  {
    pos := 0

    for i := range nums{
        if nums[i] != 0 {
            nums[pos] = nums[i]
            pos++
        }
    }

    for ; pos < len(nums); {
        nums[pos] = 0
        pos ++
    }
    return
}