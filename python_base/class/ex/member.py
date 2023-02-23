from datetime import date

class Member(object):
    def __init__(self, name, birthdate):
        self._name = name
        self._birthdate = birthdate

    def name(self):
        return self._name

    def age(self):
        # Naive and buggy
        return date.today().year - self._birthdate.year

    def greet(self):
        return f'Name: {self.name()}, Age: {self.age()}'

class Teacher(Member):
    def __init__(self, name, birthdate, teaches):
        super().__init__(name, birthdate)
        self._lecture = teaches

    def teaches(self):
        return self._lecture

    def greet(self):
        return f'{super().greet()}, Teaches: {self.teaches()}'

class Student(Member):
    def __init__(self, name, birthdate, id_no):
        super().__init__(name, birthdate)
        self._id_no = id_no

    def ID_no(self):
        return self._id_no

    def greet(self):
        return f'{super().greet()}, ID_no: {self.ID_no()}'

# Adding a new class under Student
class Visiting(Student):
    def __init__(self, name, birthdate, id_no, valid_thru):
        super().__init__(name, birthdate, id_no)
        self._valid_thru = valid_thru

    def greet(self):
        return f'{super().greet()}, Valid thru {self._valid_thru}'

    def expired(self):
        today = date.today()
        return today > self._valid_thru

members = [
    Teacher('Harry', date(1971, 12, 7), "Programming Languages"),
    Teacher('Natasha', date(1975, 9, 21), "Forbidden Archeology"),
    Student('YK', date(1999, 3, 16), 2051),
    Student('SH', date(2000, 10, 5), 4968),
    Visiting('Alice', date(1995, 7, 14), 9595, valid_thru=date(2019, 12, 25)),
    Visiting('Vanessa', date(1998, 3, 27), 9598, valid_thru=date(2019, 2, 28))
]

print("A few CAU members...")
for member in members:
    print(member.greet())
print()

members_sorted_on_age = sorted(members, key=lambda m: m.age())
print("Members sorted on age...")

for member in members_sorted_on_age:
    print(member.greet())
print()

members_sorted_on_name = sorted(members, key=lambda m: m.name().lower(), reverse=True)
print("Members sorted in reverse on name...")
for member in members_sorted_on_name:
    print(member.greet())

