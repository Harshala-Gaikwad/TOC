#Design a program for creating a machine which accepts string having equal no. of 1's and 0's

s = input("Enter the String: ")
if s.count('1')==s.count('0'):
    print("Accepted")
else:
    print("Rejected")
