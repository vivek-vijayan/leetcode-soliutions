'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
'''

# a is the string that we get from user


def is_valid(string: str):
    stack = []  # Stack to manage the bracket
    open_brackets = ['{', '[', '(']
    close_brackets = ['}', ']', ')']
    
    if len(string) < 2:  # Finding if the given string is greater that 2 else return False
        return False
    
    for x in string:
        if x in open_brackets:
            stack.append(x)
        else:
            if len(stack) > 0:
                if stack[-1] in open_brackets:
                    if open_brackets.index(stack[-1]) == close_brackets.index(x):
                        stack.pop()
                    else:
                        return False
            else:
                return False
    return False if len(stack) > 0 else True
