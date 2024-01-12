#fbonacci sequence
# 0 1 1 2 3 5 8 13 .......

def main():
    number = int(input("enter the number to discover the Nth Fibonacci: "))
    n = fibo(number)
    print(f"Fibonacci number is : {n}")

def fibo(n):
    if(n<=3):
        if(n==1):
            x=0
        elif(n==2):
            x=1
        elif(n==3):
            x=1
    else:
        x= fibo(n-1)+fibo(n-2)
    
    return x


main()