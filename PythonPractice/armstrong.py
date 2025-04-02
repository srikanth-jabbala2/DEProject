num = input("Enter a number: ")
order = len(num)
sum = 0
temp = int(num)
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10
if int(num) == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")