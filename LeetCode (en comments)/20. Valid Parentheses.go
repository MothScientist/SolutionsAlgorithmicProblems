func pop(arr *[]rune) rune {
	val := (*arr)[len(*arr)-1]
	*arr = (*arr)[:len(*arr)-1]
	return val
}

func isValid(s string) bool {
    if len(s) == 1 {
        return false
    }
    var stack []rune
    for _, c := range s {
        if (c == '(' || c == '[' || c == '{') {
            stack = append(stack, c)
        } else {
            if len(stack) == 0{
                return false
            }
            val := pop(&stack)
            concat := string(val) + string(c)
            if (concat == "()" || concat == "[]" || concat == "{}") {
                continue
            } else {
                return false
            }
        }
    }
    return len(stack)==0
}