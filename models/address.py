class Address:
    addresses = []
    next_id = 1

    def __init__(self, street,city, postal_code, id=None):
        if id is not None:
            self.id = id
            if id >= Address.next_id:
                Address.next_id = id + 1
        else:
            self.id = Address.next_id
            Address.next_id += 1
        self.street = street
        self.city = city
        self.postal_code = postal_code

    @classmethod
    def create(cls, street, city, postal_code, id=None):
        address = cls(street, city, postal_code, id)
        cls.addresses.append(address)
        return address

    @classmethod
    def delete(cls, address):
        for address in cls.addresses:
            if id(address) == id(address):
                cls.addresses.remove(address)
                return
        else:
            raise ValueError("Address not found in the list.")

    @classmethod
    def get_all(cls):
        return cls.addresses

    @classmethod
    def find_by_id(cls, address_id):
        for address in cls.addresses:
            if address_id == address.id:
                return address
        raise ValueError("Address not found with the given ID.")


    def copy(self):
        return Address(self.street, self.city, self.postal_code, self.id)

    @classmethod
    def search(cls, keyword):
        return [address for address in cls.addresses if keyword in str(address)]

    def __str__(self):
        return f"{self.street}, {self.city}, {self.postal_code}"
