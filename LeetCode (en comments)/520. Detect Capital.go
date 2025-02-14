func detectCapitalUse(word string) bool {
    allUpper := strings.ToUpper(word)
    allLower := strings.ToLower(word)
    firstUpper := strings.ToUpper(string(word[0])) + strings.ToLower(word)[1:]
    
    return word == allUpper || word == allLower || word == firstUpper

}