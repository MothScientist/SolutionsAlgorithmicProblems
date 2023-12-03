class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        split_str = dict(zip(indices, list(s)))
        answer = ""
        for i in range(len(s)):
            answer += split_str[i]
        return answer