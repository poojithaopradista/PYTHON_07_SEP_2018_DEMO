nums = []  # Empty list

while True:
    num = int(input("Enter a number:"))
    if num == 0:
        break

    nums.append(num)


nums.sort()

for n in nums:
    print(n)

print(nums)