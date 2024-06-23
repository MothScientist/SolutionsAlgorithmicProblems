func containsNearbyDuplicate(nums []int, k int) bool {
    indexMap := make(map[int]int)

    for ind, val := range nums {
        _, isExist := indexMap[val]
        if isExist && (ind - indexMap[val] <= k){
            return true
        } else {
            indexMap[val] = ind
        }
    }
    return false
}