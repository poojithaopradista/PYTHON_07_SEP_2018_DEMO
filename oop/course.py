class Course:
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

    def get_course_fee(self):
        return self.__fee * 1.12


if __name__ == "__main__":
    # using Course class
    c1 = Course("Python", 40, 4000)  # create object of Course type
    c1._Course__fee = 1000
    c1.print_details()  # call method
    print(c1.get_course_fee())
    c2 = Course("Angular", 15, 2000)
    c2.print_details()
    print(c1)
