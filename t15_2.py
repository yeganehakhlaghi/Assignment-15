pascal = []

n=int(input("Enter the number of rows:"))

for i in range(1,n+1):
    pascal.append([1]*(i))

#print (pascal)

for i in range(2,n):  
    for j in range(1,i):
       pascal[i][j]=pascal[i-1][j-1]+pascal[i-1][j]



for i in range (n):
    print(pascal[i])
