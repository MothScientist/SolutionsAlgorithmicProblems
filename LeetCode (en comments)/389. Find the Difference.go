// 1
func findTheDifference(s string, t string) byte {
    letter_count := make(map[rune]int)

    for _, char := range s {
		letter_count[char]++
	}

	for _, char := range t {
		if letter_count[char] == 0 {
			return byte(char)
		}
        letter_count[char]--
    }   
    return byte(0)
}

// 2
func findTheDifference(s string, t string) byte {
    var res byte

    for i := 0; i < len(s); i++ {
        res += t[i] - s[i] // when the strings are similar, the number will tend to zero
    }

    return res + t[len(t)-1] // t[len(t)-1] in case of a string that is 1 character longer

}