from collections import deque

stack=deque()

def isBalanced(str):
    for ch in str:
        if ch=='(' or ch=='{' or ch=='[':
            stack.append(ch)
        elif ch==')' or ch=='}' or ch==']':
            if len(stack)==0:
                return False

            opening_ch=stack.pop()
            if(ch==')'):
                if opening_ch!='(':
                    return False;
            elif(ch=='}'):
                if opening_ch!='{':
                    return False;
            elif(ch==']'):
                if opening_ch!='[':
                    return False;

    return True

if __name__=="__main__":
    str='[a+b]*(x+2y)*{gg+kk}'
    if isBalanced(str):
        print("Balanced")
    else:
        print("Not balanced")


# is_balanced("({a+b})")     --> True
# is_balanced("))((a+b}{")   --> False
# is_balanced("((a+b))")     --> True
# is_balanced("))")          --> False
# is_balanced("[a+b]*(x+2y)*{gg+kk}") --> True
                