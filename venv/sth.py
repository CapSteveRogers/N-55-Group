class XCelestialPlatform:
    def __init__(self, courses_list, users):
        self.courses_list = courses_list
        self.users = users

    def __str__(self):
        print("\nXCelestialPlatform offers the following courses: ")
        for index, course in enumerate(self.courses_list, start=1):
            print(f"{index}. {course.name} - Age Requirement: {course.min_age_requirement}")

    def authenticate_user(self, username, password):
        if username in self.users and self.users[username] == password:
            print(f"Welcome back, {username}!")
            return True
        else:
            print("Invalid username or password.")
            return False

    def add_new_user(self):
        name_input = input("Enter your full name: ")
        age_input = int(input("Enter your age: "))
        username_input = input("Enter a username (you will use it to log in): ")
        password_input = input("Enter a strong password: ")

        if username_input not in self.users:
            self.users[username_input] = password_input
            print(f"User {name_input} has been successfully signed up!")
        else:
            print("Username already exists. Please choose a different username.")

    def show_courses(self):
        self.__str__()


class Courses:
    def __init__(self, name, min_age_requirement, space_available):
        self.name = name
        self.min_age_requirement = min_age_requirement
        self.space_available = space_available
        self.students_list = []

    def __str__(self):
        return f"{self.name} (Min Age: {self.min_age_requirement}, Space Available: {self.space_available})"

    def show_students_list(self):
        if not self.students_list:
            print(f"No students have registered for {self.name} yet.")
        else:
            print(f"\nList of students attending {self.name}:")
            for index, student in enumerate(self.students_list, start=1):
                print(f"{index}. {student}")

    def add_student(self, student, age):
        if len(self.students_list) < self.space_available:
            if age >= self.min_age_requirement:
                self.students_list.append(student)
                print(f"{student} has been successfully registered for {self.name}.")
            else:
                print(f"Minimum age requirement for {self.name} is {self.min_age_requirement}.")
        else:
            print(f"The class {self.name} is already full! Please choose another class.")

    def del_student(self, student):
        if student in self.students_list:
            self.students_list.remove(student)
            print(f"{student} has been removed from {self.name}.")
        else:
            print(f"{student} is not enrolled in {self.name}.")


def main():
    # Initial platform data
    class1 = Courses("Physics", 18, 2)
    class2 = Courses("Computer Science", 15, 2)
    class3 = Courses("Intro to Statistics", 18, 2)
    class4 = Courses("Mechanical Engineering", 20, 2)

    courses_list = [class1, class2, class3, class4]
    users = {"Steve11": "2005!", "AhmedTurk": "father111", "EricCA11": "Mathews1982", "JohnSimon": "SimonJohn1999"}

    platform = XCelestialPlatform(courses_list, users)

    while True:
        print("\nWelcome to the XCelestialPlatform!")
        print("1. View Courses")
        print("2. Sign Up")
        print("3. Log In")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            platform.show_courses()

        elif choice == "2":
            platform.add_new_user()

        elif choice == "3":
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            if platform.authenticate_user(username, password):
                platform.show_courses()
                course_choice = int(input("\nWhich course would you like to enroll in? (Enter course number): ")) - 1

                if 0 <= course_choice < len(platform.courses_list):
                    selected_course = platform.courses_list[course_choice]
                    age = int(input("Enter your age: "))
                    selected_course.add_student(username, age)

                    view_students = input("Would you like to view the students attending this course? (yes/no)? ")
                    if view_students == "yes":
                        selected_course.show_students_list

                    else:
                        print("Thanks for signing up for this course!")

                else:
                    print("Invalid course selection.")

        elif choice == "4":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    main()
