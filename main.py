from person import Person
from address import Address

# Main functionality goes here
address1 = Address.create("Ngara", "Nairobi", "23568-00625")
address2 = Address.create("Kikuyu", "Kiambu", "54987-230147")
address3 = Address.create("Uthiru", "Kiambu", "54987-231147")
address4 = Address.create("Kinoo", "Kiambu", "54987-230247")
# Creating instances of Person
person1 = Person.create("Stacy", 30, "0735642987","Mpesa", address1)
person2 = Person.create("Ivan", 25, "0798423697","Card", address2)
person3 = Person.create("Cynthia", 35, "0742367897","Cash on delivery", address3)
person4 = Person.create("Israel", 18, "0710273274","Card", address4)


# Deleting a person
#Person.delete(person1)

# Getting all addresses
all_addresses = Address.get_all()
for address in all_addresses:
    print(address)

    # Getting all names
all_people = Person.get_all()
for person in all_people:
    print(person)


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
search_results = Person.search("Israel")
for result in search_results:
    print(result)
