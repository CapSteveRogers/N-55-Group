import bcrypt


class User:
    def __init__(self, email, password):
        self.email = email
        self.password = self.hash_password(password)
        self.admin = False
        self.teacher = False
        self.student = False
        self.name = None

    @staticmethod
    def hash_password(password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

    def log_in(self, email, password):
        return self.email == email and self.check_password(password)


def sign_up():
    print("\nRo'yxatdan o'tish:")
    print("1. Admin")
    print("2. O'qituvchi")
    print("3. Talaba")

    choice = input("Rolingizni tanlang (1/2/3): ")

    email = input("Emailingizni kiriting: ")

    if any(user.email == email for user in registered_users):
        print("Bu email allaqachon ro'yxatdan o'tgan. Iltimos, boshqa email foydalaning.")
        return

    password = input("Parolingizni kiriting: ")
    name = input("Ismingizni kiriting: ")

    if choice == "1":
        admin_id = input("Admin ID'ingizni kiriting: ")
        new_user = Admin(email, password, admin_id, name)
    elif choice == "2":
        subject = input("O'qitayotgan fanningizni kiriting: ")
        new_user = Teacher(email, password, subject, name)
    elif choice == "3":
        grade = input("Sizning sinfingizni kiriting: ")
        new_user = Student(email, password, grade, name)
    else:
        print("Noto'g'ri tanlov. Iltimos, qaytadan harakat qiling.")
        return

    registered_users.append(new_user)
    print(f"Ro'yxatdan o'tish muvaffaqiyatli! Siz endi {new_user.name} sifatida ro'yxatdan o'tdingiz.")


def login():
    email = input("Emailingizni kiriting: ")
    password = input("Parolingizni kiriting: ")

    for user in registered_users:
        if user.log_in(email, password):
            if user.admin:
                print(f"Xush kelibsiz, Admin {user.name}!")
            elif user.teacher:
                print(f"Xush kelibsiz, O'qituvchi {user.name}!")
            elif user.student:
                print(f"Xush kelibsiz, Talaba {user.name}!")
            return
        else:
            print("Noto'g'ri email yoki parol")


class Admin(User):
    def __init__(self, email, password, admin_id, name):
        super().__init__(email, password)
        self.admin_id = admin_id
        self.name = name
        self.admin = True


class Teacher(User):
    def __init__(self, email, password, subject, name):
        super().__init__(email, password)
        self.subject = subject
        self.name = name
        self.teacher = True


class Student(User):
    def __init__(self, email, password, grade, name):
        super().__init__(email, password)
        self.grade = grade
        self.name = name
        self.student = True


registered_users = [
    Teacher("teacher@xplatform.com", "etaplace88@", "Tarix", "Jonah Hill"),
    Teacher("teacher2@xplatform.com", "teleport.uz777", "Fizika", "Alex Brown"),
    Teacher("teacher3@xplatform.com", "happyteacher!#9", "Matematika", "Margo Robbie"),
    Admin("admin@xplatform.com", "1234ok!", "4433782", "Admin Bir"),
    Admin("admin2@xplatform.com", "hihowareyou111!", "8901233", "Admin Ikki"),
    Admin("admin3@xplatform.com", "IamAdminHere90*", "3989153", "Admin Uch"),
    Student("alice@example.com", "password123", "11", "Alice Smith"),
    Student("bob@example.com", "securePass456", "9", "Bob Johnson"),
    Student("charlie@example.com", "myPass789", "11", "Charlie Brown"),
    Student("dave@example.com", "daveIsCool!2024", "10", "Dave Wilson")
]


def main():
    while True:
        print("\nX Ta'lim Platformasi:")
        print("1. Ro'yxatdan o'tish")
        print("2. Kirish")
        print("3. Chiqish")
        choice = input("Tanlovingizni tanlang: ")

        if choice == "1":
            sign_up()

        elif choice == "2":
            login()

        elif choice == "3":
            print("Platformadan chiqyapsiz. Xayr!")
            break

        else:
            print("Noto'g'ri tanlov. Iltimos, qaytadan harakat qiling.")


if __name__ == "__main__":
    main()
