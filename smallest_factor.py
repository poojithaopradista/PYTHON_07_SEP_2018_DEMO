# Display smallest factor for a number other than 1

num = int(input("Enter a number :"))

for i in range(2, num // 2 + 1):
    if num % i == 0:
        print(f"Smallest Factor = {i}")
        break
else:
    print(f"Smallest Factor = {num}")
