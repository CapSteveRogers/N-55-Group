class ATM:
    def __init__(self, card_number, password, balance=0):
        self.card_number = card_number
        self.password = password
        self.balance = balance


def authenticate(self, input_card_number, input_password):
    return self.card_number == input_card_number and self.password == input_password  # combines both conditions


def check_balance(self):
    print(f"Hisobingizda {self.balance} pul bor")


def deposit(self, amount):
    if amount > 0:
        self.balance += amount
        print(f"Hisobingizga {amount} qo'shildi! Yangi balans: {self.balance}")
    else:
        print("1 dan kichik sonni deposit qilib bo'lmaydi!")


def withdraw(self, amount):
    if amount > 0:
        if amount <= self.balance:
            self.balance -= amount
            print(f"Hisobingizdan {amount} yechib olindi! Yangi balans: {self.balance}")
        else:
            print("Hisobingizda uncha pul mavjud emas!")
    else:
        print("1 dan kichik sonni yechib olib bo'lmaydi!")


def atm_menu():
    first_card = ATM("431230023", "dogi123!", 1500)
    second_card = ATM("332899058", "yeah993^%", 2500)

    cards = [first_card, second_card]

    print("Xush kelibsiz! Bank kartangizni kiriting.")
    input_card_number = input("Kartangiz raqamini kiriting: ")
    input_password = input("Parolingizni kiriting: ")

    authenticated_card = None
    for card in cards:
        if card.authenticate(input_card_number, input_password):
            authenticated_card = card
            break

    if authenticated_card:
        print("Muvaffaqiyatli kirish!")
        while True:
            print("\nBankamat Menyusi:")
            print("1. Balans Tekshirish")
            print("2. Pul Qo'shish")
            print("3. Pul Yechib Olish")
            print("4. Chiqish")

            choice = input("1-4 gacha bo'lgan variantni tanlang: ")

            if choice == '1':
                authenticated_card.check_balance()

            elif choice == '2':
                amount = float(input("Necha pul qo'shmoqchisiz? "))
                authenticated_card.deposit(amount)

            elif choice == '3':
                amount = float(input("Necha pul yechib olmoqchisiz? "))
                authenticated_card.withdraw(amount)

            elif choice == '4':
                print("Tanlovingiz uchun rahmat!")
                break

            else:
                print("Noto'g'ri tanlov! Boshqattan urinib ko'ring!")
    else:
        print("Noto'g'ri kart raqami yoki parol! Kirish muvaffaqiyatsiz bo'ldi.")


atm_menu()