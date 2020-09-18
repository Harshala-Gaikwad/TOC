#Design a program for creating machine that accepts the string always ending with 101

s = input("Enter the string: ")
if len(s)<3:
    print("Rejected")
else:
    n = len(s)
    if s[n-3:]=="101":
        print("Accepted")
    else:
        print("Rejected")
