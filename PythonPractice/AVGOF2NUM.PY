'''def compute_avg(a,b):
    return (a+b)/2

# Driver Code
if __name__ == "__main__":
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    avg = compute_avg(a,b)
    print("The average of",a,"and",b,"is",avg) '''

INT_MAX1=2147483647
INT_MAX2=2147483648
def compute_avg(a,b):
    return (a//2 + b//2 + (a%2 + b%2)//2)

if __name__ == "__main__":
    a = INT_MAX1
    b = INT_MAX2
    print("Actual average : ", (a+b)/2)
    print( "Computed average : ",
			compute_avg(a, b))