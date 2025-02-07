import json
import os

# File to store contacts
CONTACTS_FILE = "contacts.json"

def load_contacts():
    """Load contacts from the file."""
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return {}

def save_contacts(contacts):
    """Save contacts to the file."""
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    """Add a new contact."""
    name = input("Enter the contact's name: ").strip()
    if name in contacts:
        print("Contact already exists!")
        return

    phone = input("Enter the contact's phone number: ").strip()
    email = input("Enter the contact's email: ").strip()

    # Validate phone and email (basic validation)
    if not phone.isdigit() or len(phone) != 10:
        print("Invalid phone number! Please enter a 10-digit number.")
        return
    if "@" not in email or "." not in email:
        print("Invalid email address!")
        return

    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully!")

def search_contact(contacts):
    """Search for a contact by name."""
    name = input("Enter the name to search: ").strip()
    if name in contacts:
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
    else:
        print(f"Contact '{name}' not found!")

def update_contact(contacts):
    """Update an existing contact."""
    name = input("Enter the name of the contact to update: ").strip()
    if name not in contacts:
        print(f"Contact '{name}' not found!")
        return

    print("Leave the field blank to keep the existing value.")
    phone = input(f"Enter new phone number (current: {contacts[name]['phone']}): ").strip()
    email = input(f"Enter new email (current: {contacts[name]['email']}): ").strip()

    # Update only if new values are provided
    if phone:
        if not phone.isdigit() or len(phone) != 10:
            print("Invalid phone number! Please enter a 10-digit number.")
            return
        contacts[name]["phone"] = phone
    if email:
        if "@" not in email or "." not in email:
            print("Invalid email address!")
            return
        contacts[name]["email"] = email

    save_contacts(contacts)
    print(f"Contact '{name}' updated successfully!")

def display_menu():
    """Display the main menu."""
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Exit")

def main():
    """Main function to run the contact management system."""
    contacts = load_contacts()

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            update_contact(contacts)
        elif choice == "4":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
