class Person:
    people = []

    def __init__(self, name, age, phone_number, payment_mode, address=None):
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.payment_mode = payment_mode
        self.address = address

    @classmethod
    def create(cls, name, age, phone_number, payment_mode, address=None):
        person = cls(name, age, phone_number, payment_mode, address)
        cls.people.append(person)
        return person

    @classmethod
    def delete(cls, person):
        cls.people.remove(person)

    @classmethod
    def get_all(cls):
        return cls.people

    @classmethod
    def find_by_id(cls, person_id):
        for person in cls.people:
            if person_id == id(person):
                return person
        return None

    def copy(self):
        return Person(self.name, self.age, self.phone_number, self.payment_mode, self.address.copy() if self.address else None)

    @classmethod
    def search(cls, keyword):
        return [person for person in cls.people if keyword in person.name]

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Phone Number: {self.phone_number}, Payment Mode: {self.payment_mode}, Address: {self.address}"
