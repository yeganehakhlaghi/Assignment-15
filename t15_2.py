pascal = [[1]]

n=int(input("Enter the number of rows:"))

print(pascal[0]) 

for i in range(1,n+1):
    pascal.append([1])

    for j in range(len(pascal[i-1])-1):
        pascal[i].append(pascal[i-1][j]+pascal[i-1][j+1])
       
    pascal[i].append(1)
    print(pascal[i])