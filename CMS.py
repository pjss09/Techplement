import json
class ContactManager:
    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_contacts(self):
        with open(self.filename, "w") as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self, name, phone, email):
        if name in self.contacts:
            print("Contact already exists.")
            return
        self.contacts[name] = {"phone": phone, "email": email}
        self.save_contacts()
        print("Contact added successfully.")

    def search_contact(self, query):
        found = False
        for contact_name, contact in self.contacts.items():
            if query.lower() in contact_name.lower() or query in contact["phone"]:
                print(f"Name: {contact_name}\nPhone: {contact['phone']}\nEmail: {contact['email']}\n")
                found = True
        if not found:
            print("Contact not found.")

    def update_contact(self, name, phone=None, email=None):
        if name not in self.contacts:
            print("Contact not found.")
            return
        if phone:
            self.contacts[name]["phone"] = phone
        if email:
            self.contacts[name]["email"] = email
        self.save_contacts()
        print("Contact updated successfully.")

    def display_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return
        for name, details in self.contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")


if __name__ == "__main__":
    cm = ContactManager()
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Display All Contacts")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            cm.add_contact(name, phone, email)
        elif choice == "2":
            query = input("ENTER A NAME OR PHONE NO. TO SEARCH: ")
            cm.search_contact(query)
        elif choice == "3":
            name = input("Enter name to update: ")
            phone = input("Enter new phone (press Enter to skip): ")
            email = input("Enter new email (press Enter to skip): ")
            cm.update_contact(name, phone if phone else None, email if email else None)
        elif choice == "4":
            cm.display_contacts()
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
