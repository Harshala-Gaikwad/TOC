#Design a program to find 2's complement of a given binary no.

n = list(input("Enter a binary no.: "))
l = len(n)
n = "".join(['1' if i=='0' else '0' for i in n])
n = bin(int(n,2)+1).replace("0b","")
if l!=len(n):
    n="0"*(l-len(n))+n
print("Tow's Complement = ",n)

