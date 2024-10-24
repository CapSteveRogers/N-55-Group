class Room:
    def __init__(self, number, price, booked):
        self.number = number
        self.price = float(price[1:])
        self.booked = booked

    def __str__(self):
        return f"{self.number}-xona narxi ${self.price}"


class Hotel:
    def __init__(self, name, rating, phone_number):
        self.name = name
        self.rating = rating
        self.phone_number = phone_number
        self.rooms = []

    def __str__(self):
        return f"{self.name}: {self.rating} ({self.phone_number})"

    def show_free_rooms(self):
        free_rooms = [room for room in self.rooms if not room.booked]
        if free_rooms:
            for index, room in enumerate(free_rooms, start=1):
                print(f"{index}: {room}")
        else:
            print("Hozirda bo'sh xonalar yo'q.")

    def show_booked_rooms(self):
        booked_rooms = [room for room in self.rooms if room.booked]
        if booked_rooms:
            print("\nBand qilingan xonalar: ")
            for index, room in enumerate(booked_rooms, start=1):
                print(f"{index}: {room}")
        else:
            print("Barcha xonalar bo'sh.")

    def add_room(self, room: object):
        self.rooms.append(room)

    def del_room(self, room: object):
        if room in self.rooms:
            self.rooms.remove(room)


class Client:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def can_afford(self, room_price):
        return self.balance >= room_price

    def deduct_balance(self, amount):
        if self.can_afford(amount):
            self.balance -= amount
            return True
        return False

    def __str__(self):
        return f"Mijoz {self.name}, Balans: ${self.balance}"


Hayat = Hotel("Hayat Regency", "5 Yulduz", "71 207 12 34")
hayat_room_1 = Room("12", "$350", True)
hayat_room_2 = Room("56", "$450", False)
hayat_room_3 = Room("42", "$600", False)
hayat_room_4 = Room("72", "$500", True)
hayat_room_5 = Room("10", "$120", False)
Hayat.rooms = [hayat_room_1, hayat_room_2, hayat_room_3, hayat_room_4, hayat_room_5]

Wyndham = Hotel("Wyndham", "4 Yulduz", "78 120 37 00")
wyndham_room_1 = Room("5", "$400", False)
wyndham_room_2 = Room("19", "$200", False)
wyndham_room_3 = Room("67", "$220", True)
wyndham_room_4 = Room("12", "$450", False)
wyndham_room_5 = Room("56", "$300", True)
Wyndham.rooms = [wyndham_room_1, wyndham_room_2, wyndham_room_3, wyndham_room_4, wyndham_room_5]


def main():
    hotels = [Hayat, Wyndham]
    clients = []

    print("\nMehmonxona menyusiga xush kelibsiz!")

    client_name = input("Ismingizni kiriting: ")
    client_balance = float(input("Boshlang'ich balansingizni kiriting: "))
    current_client = Client(client_name, client_balance)
    clients.append(current_client)

    while True:
        print("\n1. Mehmonxonalarni ko'rish")
        print("2. Chiqish")

        main_question = input("Tanlang (1-2): ")
        if main_question == "1":
            for item in hotels:
                print(item)
            book_place = input("Xona band qilishni xohlaysizmi? (ha/yo'q): ")

            if book_place.lower() == "ha":
                hotel_choice = input("Qaysi mehmonxona? ").lower()
                selected_hotel = None
                for hotel in hotels:
                    if hotel.name.lower() == hotel_choice:
                        selected_hotel = hotel
                        break

                if selected_hotel:
                    print(f"\nMana {selected_hotel.name} mehmonxonasidagi bo'sh xonalar:")
                    selected_hotel.show_free_rooms()

                    room_choice = input("Band qilish uchun xona raqamini tanlang: ")
                    room_selected = None
                    for room in selected_hotel.rooms:
                        if room.number == room_choice and not room.booked:
                            room_selected = room
                            break

                    if room_selected:
                        if current_client.can_afford(room_selected.price):
                            print(f"\n{selected_hotel.name} mehmonxonasida {room_selected.number}-xonani band qilmoqdasiz.")
                            room_selected.booked = True
                            current_client.deduct_balance(room_selected.price)
                            print(f"Xona muvaffaqiyatli band qilindi! Qolgan balans: ${current_client.balance:.2f}")
                        else:
                            print("Xonani band qilish uchun yetarli mablag'ingiz yo'q.")
                    else:
                        print("Noto'g'ri xona tanlovi yoki xona band qilingan.")
                else:
                    print("Mehmonxona topilmadi. Iltimos qayta urinib ko'ring.")

            elif book_place.lower() == "yo'q":
                print("Asosiy menyuga qaytish!")
                continue

            else:
                print("Noto'g'ri kiritish! Iltimos, qayta urinib ko'ring!")

        elif main_question == "2":
            print("Bizning sahifamizga tashrif buyurganingiz uchun rahmat!")
            break

        else:
            print("Noto'g'ri kiritish! Iltimos, qayta urinib ko'ring!")


if __name__ == "__main__":
    main()
