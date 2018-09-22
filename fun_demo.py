def print_numbers(s=1, e=10):
    for i in range(s, e):
        print(i)


def fun1(p1, p2):
    print("p1 =", p1, " p2 = ",p2)


fun1(10, 20)  # Positional
# fun1(10)
fun1(p2=10, p1=1)  # Named

# print_numbers(10, 15)
print_numbers(5)
# print_numbers()
print_numbers(e=5, s=2)
print_numbers(2, 5)
