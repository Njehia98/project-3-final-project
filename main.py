from customer import Person
from address import Address
from review import Review

def display_menu():
    print("1. Create a person")
    print("2. Delete a person")
    print("3. Display all people")
    print("4. Find person by ID")
    print("5. Find person by name")
    print("6. Copy person")
    print("7. Create an address")
    print("8. Delete an address")
    print("9. Display all addresses")
    print("10. Find address by ID")
    print("11. Search for addresses")
    print("12. Copy Address")
    print("13. Create a review")
    print("14. Exit")

def create_person():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    phone_number = input("Enter phone number: ")
    payment_mode = input("Enter payment mode: ")
    person = Person.create(name, age, phone_number, payment_mode)
    print(f"Person created successfully. ID: {person.id}")

def delete_person():
    try:
        person_name = input("Enter person name to delete: ")
        person = None
        for p in Person.people:
            if p.name == person_name:
                person = p
                break
        if person:
            Person.delete(person.id)
            print("Person deleted successfully.")
        else:
            print("Person not found.")
    except ValueError as e:
        print(e)
    

def display_all_people():
    if len(Person.people) > 0:
        for person in Person.people:
            print(person)
    else:
        print("No people found.")

def find_person_by_id():
    try:
        person_id = int(input("Enter person ID to find: "))
        person = Person.find_by_id(person_id)
        print(person)
    except ValueError as e:
        print(e)

def find_person_by_name():
    try:
        person_name = input("Enter person name to find: ")
        for person in Person.people:
            if person.name == person_name:
                print(person)
                return
        print("Person not found.")
    except ValueError as e:
        print(e)


def copy_person():
    try:
        person_id = int(input("Enter person ID to copy: "))
        person = Person.find_by_id(person_id)
        copied_person = person.copy()
        print("Person copied successfully.")
        print(copied_person)
    except ValueError as e:
        print(e)

def create_address():
        street = input("Enter street: ")
        city = input("Enter city: ")
        postal_code = input("Enter postal code: ")
        address = Address.create(street, city, postal_code)
        print(f"Address created successfully. ID: {address.id}")

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

def copy_address():
    try:
        address_id = int(input("Enter address ID to copy: "))
        address = Address.find_by_id(address_id)
        copied_address = address.copy()
        print("Address copied successfully.")
        print(copied_address)
    except ValueError as e:
        print(e)

def create_review():
    try:
        person_id = int(input("Enter person ID to review: "))
        stars = int(input("Enter rating (1-5 stars): "))
        if stars < 1 or stars > 5:
            print("Invalid rating. Please enter a number between 1 and 5.")
            return
        comment = input("Enter optional comment: ")
        review = Review.create_review(person_id, stars, comment)
        print("Review submitted successfully.")
    except ValueError as e:
        print(e)
    
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
            copy_person()
        elif choice == "7":
            create_address()
        elif choice == "8":
            delete_address()
        elif choice == "9":
            display_all_addresses()
        elif choice == "10":
            find_address_by_id()
        elif choice == "11":
            search_for_addresses()
        elif choice == "12":
            copy_address()
        elif choice == "13":
            create_review()
        elif choice == "14":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
