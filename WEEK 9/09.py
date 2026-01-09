

student1_name = "Miguel"
student1_grade = "1.5"
student1_subject = ["Algebra", "Physics"]

student2_name = "John"
student2_grade = "1.0"
student2_subject = ["Geometry", "Physics"]

student3_name = "Mark"
student3_grade = "2.5"
student3_subject = ["Algebra", "English"]


def print_student_info(name, grade, subject):
    print(f"name: {name}  grade: {grade}  subject: {subject}")


# Example function calls (commented in the screenshot)
# print_student_info(student1_name, student1_grade, student1_subject)
# print_student_info(student2_name, student2_grade, student2_subject)
# print_student_info(student3_name, student3_grade, student3_subject)


class Student:
    def __init__(self, name, grade, subject):
        self.name = name
        self.grade = grade
        self.subject = subject

    def print_student_info(self):
        print(f"name: {self.name}  grade: {self.grade}  subject: {self.subject}")


student1 = Student("Gary", 1.25, ["Physics", "Chemistry"])
student1.print_student_info()
student2 = Student("Boy", 3.0, ["Physics", "Chemistry"])
student1.print_student_info()
student3 = Student("Judy", 2.25, ["Physics", "Chemistry"])
student1.print_student_info()

def print_student_info_function(name, grade, subject):
    print(f"name: {name} grade: {grade} subject: {subject}")


class Student:
    DEFAULT_SUBJECT = ["Basic Electronics", "Discrete Mathematics"]

    def __init__(self, name, grade, subject):
        self.name = name
        self.grade = grade
        self.subject = subject

    def print_student_info_method(self):
        print(f"name: {self.name} grade: {self.grade} subject: {self.subject}")

    @classmethod
    def create_default_student(cls, name, grade):
        print(f"name: {name} grade: {grade} subject: {cls.DEFAULT_SUBJECT}")
        return cls(name, grade, cls.DEFAULT_SUBJECT)

    @staticmethod
    def is_grade_passing(grade):
        return grade <= 3.0


if __name__ == "__main__":
    student1 = Student("Gary", 1.25, ["Physics", "Chemistry"])
    student1.print_student_info_method()

    if Student.is_grade_passing(student1.grade):
        print("pass")
    else:
        print("fail")

    student2 = Student.create_default_student("Marivic", 1.50)


    class Student:
        def __init__(self, name, grade, subject):
            self.name = name
            self.grade = grade
            self.subject = subject

        def print_student_info_method(self):
            print(f"{self.name} grade: {self.grade}")

        @staticmethod
        def is_grade_passing(grade):
            return grade <= 3.0


    if __name__ == "__main__":
        student1 = Student("Ferrer", 1.00, ["Physics", "Chemistry"])
        student1.print_student_info_method()
        if Student.is_grade_passing(student1.grade):
            print("pass")
    if __name__ == "__main__":
        student1 = Student("Gary", 5.00, ["Physics", "Chemistry"])
        student1.print_student_info_method()
        if Student.is_grade_passing(student1.grade):
            print("pass")
        else:
            print("fail")

        student2 = Student("Boy", 5.00, ["Physics", "Chemistry"])
        student2.print_student_info_method()
        if Student.is_grade_passing(student2.grade):
            print("pass")
        else:
            print("fail")

        student3 = Student("Judy", 3.5, ["Physics", "Chemistry"])
        student3.print_student_info_method()
        if Student.is_grade_passing(student3.grade):
            print("pass")
        else:
            print("fail")

        # Extra grade check
        if Student.is_grade_passing(1.0):
            print("pass")
        else:
            print("fail")






import serial
import threading
import time

PORT = "COM1"
BAUDRATE = 9600

ser = serial.Serial(PORT, BAUDRATE, timeout=1)
time.sleep(2)

def send(message):
    ser.write((message + '\n').encode())
    print(f"send: {message}")

def receive():
    if ser.in_waiting > 0:
        data = ser.readline().decode('utf-8').strip()
        if data:
            print(f"receive: {data}")
            return data
    return None

def received_continuous():
    while running:
        received_data = receive()
        if received_data:
            pass  # you can process data here if needed
        time.sleep(0.1)

running = True
receiver_thread = threading.Thread(target=received_continuous)
receiver_thread.start()

try:
    while True:
        message = input("Enter message: ")
        if message:
            send(message)

 except KeyboardInterrupt:
    print("exit")

finally:
    running = False
