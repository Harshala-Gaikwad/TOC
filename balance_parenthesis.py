#Program to check balance parenthesis
open_brackets = ['[','{','(']
close_brackets = [']','}',')']
s = input("Enter the string: ")
l = []
flag = 0
for i in s:
    if i in open_brackets:
        l.append(i)
    elif i in close_brackets:
        p = close_brackets.index(i)
        if len(l)>0:
            if open_brackets[p]==l[len(l)-1]:
                l.pop()
        else:
            flag = 1
            print("Not balanced")
            break;
    else:
        print("Not a valid string")
if flag!=1:
    if len(l)==0:
        print("Balanced")
    else:
        print("Not balanced")
