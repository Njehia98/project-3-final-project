class Address:
    addresses = []

    def __init__(self, street, city, postal_code):
        self.street = street
        self.city = city
        self.postal_code = postal_code

    @classmethod
    def create(cls, street, city, postal_code):
        address = cls(street, city, postal_code)
        cls.addresses.append(address)
        return address

    @classmethod
    def delete(cls, address):
        cls.addresses.remove(address)

    @classmethod
    def get_all(cls):
        return cls.addresses

    @classmethod
    def find_by_id(cls, id):
        for address in cls.addresses:
            if id == id(address):
                return address
        return None

    def copy(self):
        return Address(self.street, self.city, self.postal_code)

    @classmethod
    def search(cls, keyword):
        return [address for address in cls.addresses if keyword in str(address)]

    def __str__(self):
        return f"{self.street}, {self.city}, {self.postal_code}"


class Person:
    people = []

    def __init__(self, name, age, address=None):
        self.name = name
        self.age = age
        self.address = address

    @classmethod
    def create(cls, name, age, address=None):
        person = cls(name, age, address)
        cls.people.append(person)
        return person

    @classmethod
    def delete(cls, person):
        cls.people.remove(person)

    @classmethod
    def get_all(cls):
        return cls.people

    @classmethod
    def find_by_id(cls, id):
        for person in cls.people:
            if id == id(person):
                return person
        return None

    def copy(self):
        return Person(self.name, self.age, self.address.copy() if self.address else None)

    @classmethod
    def search(cls, keyword):
        return [person for person in cls.people if keyword in person.name]

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Address: {self.address}"


# Example Usage:

# Creating instances of Address
address1 = Address.create("123 Main St", "Anytown", "12345")
address2 = Address.create("456 Elm St", "Another Town", "54321")

# Creating instances of Person
person1 = Person.create("Alice", 30, address1)
person2 = Person.create("Bob", 25, address2)

# Deleting a person
Person.delete(person1)

# Getting all addresses
all_addresses = Address.get_all()
for address in all_addresses:
    print(address)

# Finding a person by ID
found_person = Person.find_by_id(id(person2))
print(found_person)

# Copying a person
copied_person = person2.copy()
print(copied_person)

# Searching for persons by name
search_results = Person.search("Bob")
for result in search_results:
    print(result)
