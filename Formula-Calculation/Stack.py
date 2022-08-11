# icp -> priority of itself
# isp -> priority of the top of stack
isp = {'(': 0, ')': 19, '+': 12, '-': 12, '*': 13, '/': 13, '%': 13, '\0': 0}
icp = {'(': 20, ')': 19, '+': 12, '-': 12, '*': 13, '/': 13, '%': 13, '\0': 0}

answer = ""
target = "A*((B+C)/D)"

# postfix
stack = ['\0']
for char in target:
    # operand
    if char not in icp.keys():
        answer += char

    # right parenthesis
    elif char == ')':
        while stack and stack[-1] != '(':
            answer += stack.pop()
            stack.pop()

    # else
    else:
        if isp[stack[-1]] >= icp[char]:
            answer += stack.pop()
        else:
            stack.append(char)

# pop left elements in the stack
while stack:
    answer += stack.pop()

print(answer)
