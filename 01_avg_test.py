test1 = int(input("Enter the test1 marks : "))
test2 = int(input("Enter the test2 marks : "))
test3 = int(input("Enter the test3 marks : "))

if test1<test2 and test1<test3:
    avg = (test2+test3)/2

elif test2<test1 and test2<test3:
    avg= (test1+test3)/2

else:
    avg= (test1+test2)/2

print("avg of test1 : ",test1," test2 : ",test2, " and  test3 : ",test3, " is ",avg )
    
