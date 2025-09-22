def fib(num):
    if (num==0 or num==1):
        return num
    else:
        val=fib(num-1)+fib(num-2)
        return(val)
num=int(input("Enter how many terms of fibonacci series to be print:"))
print("\nFibonacci series :")
for i in range(num):
    result=fib(i)
    print(result)
    #