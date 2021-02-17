num=int(input("Enter the number\n"))
fact=1
if num<0:
    print("Factorial is not possible for negative numbers")
elif num==0:
    print("Fcatorial of 0 is 1")
else:
    for i in range(1,num+1):
        fact=fact*i
    print("Factorial of",num,"is",fact)