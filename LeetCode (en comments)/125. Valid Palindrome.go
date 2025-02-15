func isPalindrome(s string) bool {
    var cleaned strings.Builder
    for _, char := range strings.ToLower(s) {
        if unicode.IsLetter(char) || unicode.IsDigit(char) {
            cleaned.WriteRune(char)
        }
    }
    cleanedStr := cleaned.String()
    l := len(cleanedStr)
    for i := 0; i < l / 2; i++ {
        if cleanedStr[i] != cleanedStr[l - 1 - i] {
            return false
        }
    }
    return true
}