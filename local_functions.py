v = 10  # Module/Global


def fun1():
    print("In fun1()")
    v = 20
    # Local function
    def fun2():
        print("In fun2()", " value of v = ", v)

    print("Calling fun2()")
    fun2()
    print("Value of v = ", v)


fun1()
print("Module level v = ", v)
