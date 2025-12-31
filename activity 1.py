num = int(input("enter a number: "))
count = 0
temp = abs(num)
while temp > 0:
    count += 1
    temp //=10
print("total digits:",count)