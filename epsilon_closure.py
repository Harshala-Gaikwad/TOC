#Program to calculate epsilon closure of states in NFA
n = int(input("Enter the no. of states:"))
l,l1 = [],[]
for i in range(n):
    l.append("q"+str(i))
    x = input("Enter states with epsilon move "+"q"+str(i)+": ")
    l1.append(x)
result = []
for i in range(n):
    temp = []
    temp.append("q"+str(i))
    for j in range(i,n):
        if l1[j]=='null':
            break
        temp.append(l1[j])
    result.append(temp)
print("Epsilon Closure of:")   
for i in range(n):
    print("q"+str(i)+" = "+str(result[i]))
