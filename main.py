from person import Person
from address import Address

# Your main functionality goes here
address1 = Address.create("Ngara", "Nairobi", "23568-00625")
address2 = Address.create("Kikuyu", "Kiambu", "54987-230147")

# Creating instances of Person
person1 = Person.create("Stacy", 30, address1)
person2 = Person.create("Ivan", 25, address2)

# Deleting a person
#Person.delete(person1)

# Getting all addresses
all_addresses = Address.get_all()
for address in all_addresses:
    print(address)

# Finding a person by ID
found_person = Person.find_by_id(id(person1))
if found_person:
    print(found_person)
else:
    print("Person not found")

# Copying a person
copied_person = person2.copy()
print(copied_person)

# Searching for persons by name
search_results = Person.search("Ivan")
for result in search_results:
    print(result)
