from collections import UserDict

class Field: 
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return str(self.value)
    
class Name(Field):
    # def __init__(self, value):
    #     self.value = value
    def __init__(self, value):
        if not value.strip():
            raise ValueError("Name cannot be empty")
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        if len(value) == 10 and value.isdigit():
            super().__init__(value)
        else:
            raise ValueError("The phone didn't pass validation")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    
    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))

    def remove_phone(self, phone_number):
        self.phones = [p for p in self.phones if str(p) != phone_number]

    # TODO: Потрібно додати функції з попередньої роботи          
    def edit_phone(self, old_phone, new_phone):
        for p in self.phones: # ітерація по номерах в списку
            if p.value == old_phone: # перевіряємо чи заданий номер "дорівнює" номеру, який ми хочемо замінити
                p.value = new_phone # якщо збігається - замінюємо на новий
    
    def find_phone(self, phone):
        for p in self.phones: # ітерація по номерах в списку
            if p.value == phone: # перевірка чи заданий номер є у списку
                return p # повертаємо його
        return "Contact is missing" # повертаємо повідомлення, якщо номер не знайдено

    #Не вийшло правильно перетворити, тому написав нові методи            
    # def edit_phone(self, args):
    #     name, new_phone = args

    #     if name == self.name.value:
    #         self.phones = [new_phone]
    #         return "Contact changed!"
    #     else:
    #         return "Contact is missing"

    # def find_phone(self, args):
    #     name = args[0]
    #     if name == self.name.value:
    #         return self.phones
    #     else:
    #         return "Contact is missing"
            
    def __str__(self):
        return f"Contacts name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")
