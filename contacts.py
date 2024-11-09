def add_contact(address_book, name, phone):
    address_book[name] = phone

def search_contact(address_book, name):
    return address_book.get(name, "Contact not found")

address_book = {}

# Add a contact
add_contact(address_book, "Alice", "555-1212")

# Search for a contact
print(search_contact(address_book, "Alice"))  # Output: 555-1212
print(search_contact(address_book, "Bob"))    # Output: Contact not found
