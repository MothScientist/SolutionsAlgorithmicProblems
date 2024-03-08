func plusOne(digits []int) []int {
    for i := len(digits) - 1; i >= 0; i-- {
        
        if digits[i] < 9{
            /* 
            If there is a number (1-8) that can be increased without adding a new number, 
            then it will increase by 1 and the cycle will end. 
            */
            digits[i]++
            return digits
        }
        // If the number is 9
        digits[i] = 0
    }

    // If don't find digit in number less than 9 - add digit
    if digits[0] == 0 {
        // Adding an element to the beginning of a slice
        digits = append([]int{1}, digits...)
    }

    return digits
}