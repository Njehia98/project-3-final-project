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
    def find_by_id(cls, address_id):
        for address in cls.addresses:
            if address_id == id(address):
                return address
        return None

    def copy(self):
        return Address(self.street, self.city, self.postal_code)

    @classmethod
    def search(cls, keyword):
        return [address for address in cls.addresses if keyword in str(address)]

    def __str__(self):
        return f"{self.street}, {self.city}, {self.postal_code}"
