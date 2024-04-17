# Check if the paranthese are correctly placed and balanced 

def isBalanced(s):
    stack = []
    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack:
                return False
            if ((char == ')' and stack[-1] != '(') or 
                (char == ']' and stack[-1] != '[') or 
                (char == '}' and stack[-1] != '{')):
                return False
            stack.pop()
    return not stack

# usage of the function

a = "{2*(3+4)-(5+6)}"
print(isBalanced(a)) # True

b = "{2*(3+4-[5+6)}"
print(isBalanced(b)) # False


