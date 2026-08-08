#create class for the student information system
class student:
    def __init__(self, full_name, age, address, student_ID):

        self.full_name = full_name
        self.age = age
        self.address = address
        self.student_ID = student_ID

#student information 
    def display(self):
        print(f"Name      : {self.full_name}")
        print(f"Age       : {self.age}")
        print(f"Address   : {self.address}")
        print(f"Student ID: {self.student_id}")
        print("-" * 45)

# create class for the Student Manager
class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self):
        full_name = input("Enter full name: ")

        while True:
            try:
                age = int(input("Enter age: "))
                if age < 0:
                    print("Age cannot be negative.")
                    continue
                break
            except ValueError:
                print("Please enter a valid whole number for age.")

        address = input("Enter address: ")
        student_id = input("Enter Student ID: ")
        student = student(full_name, age, address, student_id)
        self.students.append(student)
        print("Student added successfully.\n")

#collect student information to system
    def collect_students(self):

        print("Student Information System")
        print("=" * 45)
        print("Enter 70 for exactly 70 students.")
        print("Press Enter for an unknown/dynamic number of students.\n")

        choice = input("Number of students (70 or Enter): ")
        if choice == "":
            print("\nDynamic mode selected.")
            print("Enter student information one at a time.\n")

            while True:
                self.add_student()

                another = input(
                    "Add another student? (y/n): "
                ).strip().lower()

                if another != "y":
                    break

        else:
            try:
                number_of_students = int(choice)

                if number_of_students != 70:
                    print("Please enter exactly 70 or press Enter for dynamic mode.")
                    return

                for i in range(number_of_students):
                    print(f"\nEntering student {i + 1} of {number_of_students}")
                    self.add_student()

            except ValueError:
                print("Invalid input. Please enter 70 or press Enter.")

    def sort_by_age(self):
        self.students = sorted(self.students, key=lambda student: student.age)

    def display_students(self):

        if not self.students:
            print("\nNo student records found.")
            return

        print("\nSTUDENTS SORTED BY AGE")
        print("=" * 45)

        for student in self.students:
            student.display()

    def run(self):
        self.collect_students()

        if self.students:
            self.sort_by_age()
            self.display_students()


if __name__ == "__main__":
    manager = StudentManager()

    manager.run()