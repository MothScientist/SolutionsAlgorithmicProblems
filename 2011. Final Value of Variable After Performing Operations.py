def final_value_after_operations(self, operations: list[str]) -> int:
    res = 0
    for i in operations:
        if "+" in i:
            res += 1
        else:
            res -= 1
    return res
