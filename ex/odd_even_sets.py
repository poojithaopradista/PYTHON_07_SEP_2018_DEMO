odd_nums = set()
even_nums = set()

while True:
    num = int(input("Enter a number :"))
    if num == 0:
        break

    if num % 2 == 0:
        even_nums.add(num)
    else:
        odd_nums.add(num)


for n in sorted( odd_nums | even_nums):
    print(n)