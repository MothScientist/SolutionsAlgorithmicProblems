#1
def interpret(self, command: str) -> str:
        return command.replace('()','o').replace('(al)','al')

#2
def interpret(self, command: str) -> str:
        answer_str = ""
        for i in range(len(command)):
            if command[i] != '(' and command[i] != ')':
                answer_str += command[i]
            elif command[i] == '(' and command[i+1] == ')':
                answer_str += 'o'
        return answer_str