func isPalindrome(x int) bool {
    if x < 0 {
        return false
    }
    new_x := 0
    y := x
    for y > 0 {
        new_x *= 10
        new_x += (y % 10)
        y /= 10
    }
    return new_x == x
}

func isPalindrome(x int) bool {
    if x < 0 {
        return false
    }
    num_str := fmt.Sprintf("%d", x)
    n := len(num_str)
    for i := 0; i <= n / 2; i ++ {
        if num_str[i] != num_str[n-i-1] {
            return false
        }
    }
    return true
}