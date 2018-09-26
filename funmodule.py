# Module

def fun1():
    print("In fun1() of module funmodule")


def fun2():
    print("In fun2() of module funmodule")


if __name__ == "__main__":  # run as script
    print("Module name : ", __name__)
    print("This is module - funmodule")
else:  # just imported
    print("Importing funmodule")
