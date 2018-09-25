def add_num(list, num):
    print("Address of n before : ", id(list))
    list.append(num)
    print("Address of n after change : ", id(list))


nums = [10, 20]
print(id(nums))
add_num(nums, 30)
print(nums)
