num=int(input("Enter the number\n"))
flag=0
if num>1:
    for i in range(2,num):
        if num%i ==0:
            print(num,"is not a prime number")
            flag=1
            break
    if flag == 0:
        print(num,"is a prime number")
else:
    print(num,"is not a prime number")