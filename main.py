from person import Person
from address import Address

def display_menu():
    print("1. Create a person")
    print("2. Delete a person")
    print("3. Display all people")
    print("4. Find person by ID")
    print("5. Find person by name")
    print("6. Create an address")
    print("7. Delete an address")
    print("8. Display all addresses")
    print("9. Find address by ID")
    print("10. Search for addresses")
    print("11. Exit")

def create_person():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    phone_number = input("Enter phone number: ")
    payment_mode = input("Enter payment mode: ")
    # You may prompt for address information here if needed
    Person = Person.create(name, age, phone_number, payment_mode)
    print("Person created successfully.")

def delete_person():
    try:
        person_name = int(input("Enter person name to delete: "))
        person = Person.find_by_name(person_name)
        Person.delete(person)
        print("Person deleted successfully.")
    except ValueError as e:
        print(e)

def display_all_people():
    for person in Person.get_all():
        print(person)

def find_person_by_id():
    try:
        person_id = int(input("Enter person ID to find: "))
        person = Person.find_by_id(person_id)
        print(person)
    except ValueError as e:
        print(e)

def find_person_by_name():
    try:
        person_name = int(input("Enter person name to find: "))
        person = Person.find_by_id(person_name)
        print(person)
    except ValueError as e:
        print(e)

def create_address():
    try:
        street = input("Enter street: ")
        city = input("Enter city: ")
        postal_code = input("Enter postal code: ")
        address = Address.create(street, city, postal_code)
        print("Address created successfully.")
    except ValueError as e:
        print(e)

def delete_address():
    try:
        address_id = int(input("Enter address ID to delete: "))
        address = Address.find_by_id(address_id)
        Address.delete(address)
        print("Address deleted successfully.")
    except ValueError as e:
        print(e)

def display_all_addresses():
    for address in Address.get_all():
        print(address)

def find_address_by_id():
    try:
        address_id = int(input("Enter address ID to find: "))
        address = Address.find_by_id(address_id)
        print(address)
    except ValueError as e:
        print(e)

def search_for_addresses():
    try:
        keyword = input("Enter keyword to search: ")
        addresses = Address.search(keyword)
        for address in addresses:
            print(address)
    except ValueError as e:
        print(e)
    

# Similar functions for other actions related to Person and Address classes

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            create_person()
        elif choice == "2":
            delete_person()
        elif choice == "3":
            display_all_people()
        elif choice == "4":
            find_person_by_id()
        elif choice == "5":
            find_person_by_name()
        elif choice == "6":
            create_address()
        elif choice == "7":
            delete_address()
        elif choice == "8":
            display_all_addresses()
        elif choice == "9":
            find_address_by_id()
        elif choice == "10":
            search_for_addresses()
        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
