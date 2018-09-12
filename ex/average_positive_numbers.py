
total = 0
count = 0

while True:
    num = int(input("Enter a number:"))
    if num == 0:
        break

    if num < 0:
        continue

    total += num  #  total = total + num
    count += 1


print("Average = %5.2f" % (total / count))