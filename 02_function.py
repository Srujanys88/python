def F(n):
    if n==0 or n==1:
        return 1
    return F(n-1)+ F(n-2)

n = int(input("Enter the number : "))
if n<0:
    print("Enter N>0")
    exit
for i in range(n):
    ans = F(i)
    print(ans, end="  ")
