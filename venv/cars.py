import bcrypt


class User:
    def __init__(self, email, name, password):
        self.email = email
        self.name = name
        self.admin = False
        self.teacher = False
        self.student = False
        self.is_active = False
        self.password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    def check_password(self, password):
        return bcrypt.checkpw(password.encode(), self.password)

    def change_password(self, new_password):
        self.password = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt())
        self.is_active = True


users = []


def add_user():
    print("\nBirinchi bo'lib ro'yxatdan o'ting: ")
    email = input("Emailingizni kiriting: ")
    name = input("Ismingizni kiriting: ")
    temp_password = input("Vaqtinchalik parol yarating: ")
    user1 = User(email, name, temp_password)

    print("\nKim sifatida ro'yxatdan o'tmoqchisiz:")
    print("1. O'qituvchi")
    print("2. Talaba")
    print("3. Administrator")
    role_question = input("1-3 orasida tanlang: ")
    if role_question == '1':
        user1.teacher = True
    elif role_question == '2':
        user1.student = True
    elif role_question == '3':
        user1.admin = True

    users.append(user1)
    print("Muvaffaqiyatli ro'yxatdan o'tdingiz!")


def log_in(email, password):
    for user in users:
        if user.email == email:
            if user.check_password(password):
                if not user.is_active:
                    new_password = input("Parolingiz vaqtinchalik. Yangi parol kiriting: ")
                    user.change_password(new_password)
                print("Tizimga muvaffaqiyatli kirdingiz!")
                return
            else:
                print("Noto'g'ri parol.")
                return
    print("Foydalanuvchi topilmadi.")


def process():
    while True:
        print("1. Foydalanuvchilarni ko'rish")
        print("2. Foydalanuvchi qo'shish")
        print("3. Tizimga kirish")
        print("4. Chiqish")
        main_question = input("Variantlardan birini tanlang (1-4): ")

        if main_question == '1':
            for item in users:
                print(item.email, item.name)

        elif main_question == '2':
            add_user()

        elif main_question == '3':
            email = input("Emailingizni kiriting: ")
            password = input("Parolingizni kiriting: ")
            log_in(email, password)

        elif main_question == '4':
            print("Rahmat!")
            break

        else:
            print("Noto'g'ri kirish. Qayta urinib ko'ring!")


process()
