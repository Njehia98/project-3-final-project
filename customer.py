class Person:
    people = []
    next_id = 1

    def __init__(self, name, age, phone_number, payment_mode, id=None, address=None):
        if id is not None:
            self.id = id
            if id >= Person.next_id:
                Person.next_id = id + 1
        else:
            self.id = Person.next_id
            Person.next_id += 1
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.payment_mode = payment_mode
        self.address = address

    @classmethod
    def create(cls, name, age, phone_number, payment_mode, id=None, address=None):
        person = cls(name, age, phone_number, payment_mode, id, address)
        cls.people.append(person)
        return person

    @classmethod
    def delete(cls, person_id):
        for person in cls.people:
            if person_id == person.id:
                cls.people.remove(person)
                return
        else:
            raise ValueError("Person not found in the list.")


    @classmethod
    def get_all(cls):
        return cls.people

    @classmethod
    def find_by_id(cls, person_id):
        for person in cls.people:
            if person_id == person.id:
                return person
        raise ValueError("Person not found with the given ID.")
    

    def copy(self):
        return Person(self.name, self.age, self.phone_number, self.payment_mode, self.address.copy() if self.address else None)

    @classmethod
    def search(cls, keyword):
        return [person for person in cls.people if keyword in person.name]

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Age: {self.age}, Phone Number: {self.phone_number}, Payment Mode: {self.payment_mode}, Address: {self.address}"
