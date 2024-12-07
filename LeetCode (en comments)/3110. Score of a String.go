func scoreOfString(s string) int {
    res := 0

    for i := 1; i < len(s); i++{
        res += getAbs(int(s[i - 1]), int(s[i]))
    }

    return res
}

func getAbs(a int, b int) int {
    if (a > b) {
        return a - b
    }
    return b - a
}