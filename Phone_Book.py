# Problem 3: PhoneBook
# Question:
# Design a phonebook system that supports the following operations:
#
# add_contact(name, number) — add a phone number to a contact
# find_by_name(name) — return all numbers for that contact
# find_by_number(number) — return the contact name for that number
# delete_contact(name) — remove a contact and all their numbers
# search_by_prefix(prefix) — return all contact names starting with the given prefix
#
# pb = PhoneBook()
# pb.add_contact("Alice", "647-111-2222")
# pb.add_contact("Alice", "647-333-4444")
# pb.add_contact("Bob",   "416-555-6666")
# pb.add_contact("Barry", "905-777-8888")
#
# pb.find_by_name("Alice")           → ["647-111-2222", "647-333-4444"]
# pb.find_by_number("416-555-6666")  → "Bob"
# pb.search_by_prefix("Ba")          → ["Barry"]
# pb.delete_contact("Alice")
# pb.find_by_name("Alice")           → []

class PhoneBook:
    def __init__(self):
        self.contacts = {}          # name → list of numbers
        self.number_to_name = {}    # number → name (reverse lookup)

    def add_contact(self, name, number):
        if name not in self.contacts:
            self.contacts[name] = []
        self.contacts[name].append(number)
        self.number_to_name[number] = name

    def find_by_name(self, name):
        return self.contacts.get(name, [])

    def find_by_number(self, number):
        return self.number_to_name.get(number, None)

    def delete_contact(self, name):
        if name in self.contacts:
            for number in self.contacts[name]:
                del self.number_to_name[number]
            del self.contacts[name]

    def search_by_prefix(self, prefix):
        # Return all contacts whose name starts with prefix
        return [name for name in self.contacts if name.startswith(prefix)]

    def search_number_by_prefix(self, prefix):
        # Return all numbers starting with a digit prefix
        return [num for num in self.number_to_name if num.startswith(prefix)]


# Test
pb = PhoneBook()
pb.add_contact("Alice", "647-111-2222")
pb.add_contact("Alice", "647-333-4444")  # Alice has 2 numbers
pb.add_contact("Bob",   "416-555-6666")
pb.add_contact("Barry", "905-777-8888")

print(pb.find_by_name("Alice"))          # ['647-111-2222', '647-333-4444']
print(pb.find_by_number("416-555-6666")) # 'Bob'
print(pb.search_by_prefix("Ba"))         # ['Barry']
print(pb.search_number_by_prefix("647")) # ['647-111-2222', '647-333-4444']

pb.delete_contact("Alice")
print(pb.find_by_name("Alice"))          # []