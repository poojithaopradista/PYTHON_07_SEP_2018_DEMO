class Course:
    tax = 12  # class attribute (static variable)

    # Constructor
    def __init__(self, title, duration, fee):
        # Instance or object attributes
        self.__title = title
        self.__duration = duration
        self.__fee = fee

    # Methods
    def print_details(self):
        print("Title    : ", self.__title)
        print("Duration : ", self.__duration)
        print("Fee      : ", self.__fee)

    @staticmethod
    def set_tax(newtax):
        if newtax < 0 or newtax > 50:
            raise ValueError("Invalid Tax")

        Course.tax = newtax

    @property
    def course_fee(self):
        return self.__fee + (self.__fee * Course.tax / 100)

    @course_fee.setter
    def course_fee(self, value):
        self.__fee = value


if __name__ == "__main__":
    # using Course class
    c1 = Course("Python", 40, 4000)  # create object of Course type
    c1.fee = 1000
    c1.print_details()  # call method
    print(c1.course_fee)
    Course.set_tax(15)
    print(c1.course_fee)

    c2 = Course("Angular", 15, 2000)
    c2.print_details()
    print(c1)
