sum = 0

for i in range(1, 6):
    try:
        num = int(input("Enter a number :"))
        sum += num
    except:
        print("Invalid Input")

print("Sum = ", sum)
