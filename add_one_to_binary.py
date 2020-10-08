#Design a program which will increment the given binary number by 1
n = input("Enter a binary number: ")
inc = bin(int(n,2)+1).replace("0b","")
print("Number after adding 1: ",inc)
