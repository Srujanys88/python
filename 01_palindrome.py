num = int(input("Enter a number : "))
onum = num
rev = 0
digits = list()
for i in range(10):
    digits.append(0)

while num>0:
    d = num%10
    digits[d] += 1
    rev = rev*10 + d
    num = num//10

print(rev)
if(rev == onum):
    print(onum," is palindrome")
else:
    print(onum," is not a  palindrome")

print(digits)
