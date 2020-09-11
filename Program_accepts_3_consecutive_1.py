#machine that accepts three consecutive one's
s = input("Enter the string: ")
flag = 0
for i in range(len(s)-2):
    if s[i]=='1' and s[i+1]=='1' and s[i+2]=='1':
        print("Accepted")
        flag = 1
        break;

if flag==0:
    print("Rejected")
