try:
    num = int(input("Enter a number :"))
    print(100 / num)
except (ValueError,ZeroDivisionError):
    print("Sorry! Invalid Number!")
# except ZeroDivisionError:
#    print("Sorry! Number cannot be zero!")


print("The End")
