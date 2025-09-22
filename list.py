list=[45,50,60,70,80,90,76,101]
f=int(input("Enter the k Value :"))
len=len(list)
for i in range(len):
    for j in range(i+1,len):
        if(list[i]<list[j]):
            temp=list[i]
            list[i]=list[j]
            list[j]=temp
result=list[f-1]
print(f"{f} Largest number is {result}")