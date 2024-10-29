import json
import re
from datetime import datetime, timedelta


class Room:
    def __init__(self, room_number):
        self.room_number = room_number
        self.is_booked = False
        self.client = None


class Client:
    def __init__(self, name, phone, email, booking_date=None):
        self._name = None
        self._phone = None
        self._email = None
        self.booking_date = booking_date or datetime.now()

        self.name = name
        self.phone = phone
        self.email = email

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if re.match(r"^[A-Za-z\s]{2,50}$", value):
            self._name = value
        else:
            raise ValueError("Noto‘g‘ri ism. Faqat harflardan iborat bo‘lishi va uzunligi 2-50 orasida bo‘lishi kerak.")

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        if re.match(r"^\+?[1-9]\d{1,14}$", value):
            self._phone = value
        else:
            raise ValueError("Noto‘g‘ri telefon raqami formati.")

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if re.match(r"[^@]+@[^@]+\.[^@]+", value):
            self._email = value
        else:
            raise ValueError("Noto‘g‘ri email formati.")


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.clients = []

    def add_room(self, room_number):
        new_room = Room(room_number)
        self.rooms.append(new_room)
        print(f"{room_number}-xona muvaffaqiyatli qo‘shildi.")

    def show_empty_rooms(self):
        empty_rooms = [room.room_number for room in self.rooms if not room.is_booked]
        if empty_rooms:
            print("Bo‘sh xonalar:", empty_rooms)
        else:
            print("Bo‘sh xonalar mavjud emas.")

    def show_booked_rooms(self):
        booked_rooms = [room.room_number for room in self.rooms if room.is_booked]
        if booked_rooms:
            print("Band qilingan xonalar:", booked_rooms)
        else:
            print("Xozirda band qilingan xonalar yo‘q.")

    def save_rooms_to_json(self, filename="rooms.json"):
        rooms_data = [{"room_number": room.room_number, "is_booked": room.is_booked} for room in self.rooms]
        with open(filename, 'w') as file:
            json.dump(rooms_data, file, indent=4)
        print("Xonalar ma’lumotlari JSON fayliga saqlandi.")

    def add_client(self, room_number, name, phone, email):
        room = next((room for room in self.rooms if room.room_number == room_number and not room.is_booked), None)
        if room:
            client = Client(name, phone, email)
            room.is_booked = True
            room.client = client
            self.clients.append(client)
            print(f"{name} {room_number}-xona uchun qo‘shildi.")
        else:
            print(f"{room_number}-xona allaqachon band qilingan yoki mavjud emas.")

    def show_recent_clients(self):
        cutoff_date = datetime.now() - timedelta(days=2)
        recent_clients = [client for client in self.clients if client.booking_date >= cutoff_date]
        if recent_clients:
            print("So‘nggi 2 kun ichida xona band qilgan mijozlar:")
            for client in recent_clients:
                print(
                    f"Ism: {client.name}, Telefon: {client.phone}, Email: {client.email}, Band qilish sanasi: {client.booking_date}")
        else:
            print("So‘nggi 2 kun ichida hech qanday mijoz xona band qilmagan.")


hotel = Hotel("Katta Mehmonxona")
hotel.add_room(101)
hotel.add_room(102)
hotel.add_room(103)

hotel.show_empty_rooms()

hotel.add_client(101, "Ali Akbarov", "+998901234567", "ali@example.com")
hotel.show_empty_rooms()
hotel.show_booked_rooms()

hotel.save_rooms_to_json()

hotel.add_client(102, "Bobur Karimov", "+998909876543", "bobur@example.com")
hotel.show_recent_clients()

try:
    hotel.clients[0].name = "Ali Karimov"
    hotel.clients[0].phone = "+998998765432"
    hotel.clients[0].email = "newali@example.com"
    print("Mijoz ma’lumotlari muvaffaqiyatli yangilandi.")
except ValueError as e:
    print(e)
