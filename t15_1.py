A=[]

n=int(input("Enter the size of the array:"))

for i in range(n):
    num=int(input("Enter the number:"))
    A.append(num)

flg=1

for j in range(n//2):
    if A[j]==A[n-j-1]:
        t=1

    else:
        t=0
        break

if t==1:
    print("The array is symmetric")

else:
    print("The array is not symmetric")