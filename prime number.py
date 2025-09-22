a=int(input("Enter the  start value:"))
b=int(input("Enter the end value:"))

for i in range(a,b):
    flag=0
    j=2
    while(j<i):
        if(i%j==0):
            flag=1
        j+=1
    if(flag==0):
        print(i)