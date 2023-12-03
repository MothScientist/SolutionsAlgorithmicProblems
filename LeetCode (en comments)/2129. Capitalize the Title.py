class Solution:
    def capitalizeTitle(self, title: str) -> str:
        answer = title.lower().split()
        title = ""
        for i in range(len(answer)):
            if i != 0:
                title += " "
            if len(answer[i]) > 2:
                title += answer[i].capitalize()
            else:
                title += answer[i]
        return title