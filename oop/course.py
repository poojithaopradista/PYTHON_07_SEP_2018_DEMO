class Course:
    tax = 12  # class attribute (static variable)

    # Constructor
    def __init__(self, title, duration, fee):
        # Instance or object attributes
        self.__title = title
        self.__duration = duration
        self.__fee = fee

    def __str__(self):
        return  self.__title

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


# Subclass
class OnlineCourse(Course):
    def __init__(self, title, duration, fee, url):
        super().__init__(title, duration, fee)
        self.__url = url

    # Overriding -
    def print_details(self):
        # super().print_details()
        Course.print_details(self)
        print("URL      : ", self.__url)


if __name__ == "__main__":
    # using Course class
    c1 = Course("Python", 40, 4000)  # create object of Course type
    c1.fee = 1000
    print(c1.__str__())
    # c1.print_details()  # call method

    oc1 = OnlineCourse("Angular", 20, 3000, "http://www.xyz.com/abc")
    oc1.print_details()
    # print(OnlineCourse.__bases__)
