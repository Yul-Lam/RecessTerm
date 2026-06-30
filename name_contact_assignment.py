import re
from typing import List, Dict, Optional


class ContactManager:
    def __init__(self) -> None:
        self.contacts: List[Dict[str, str]] = []

    def validate_phone(self, phone: str) -> bool:
        if not phone:
            return False
        return bool(re.fullmatch(r"\+?[0-9-]+", phone))

    def validate_email(self, email: str) -> bool:
        if not email:
            return True
        return "@" in email and "." in email

    def format_contacts(self, contacts: List[Dict[str, str]]) -> str:
        if not contacts:
            return "No contacts found."

        lines = ["Contacts:"]
        for idx, contact in enumerate(contacts, start=1):
            lines.append(
                f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact.get('email', '') or 'N/A'}"
            )
        return "\n".join(lines)

    def add_contact(self, name: str, phone: str, email: Optional[str] = None) -> bool:
        if not name.strip():
            print("Error: Name cannot be empty.")
            return False

        if not self.validate_phone(phone):
            print("Error: Phone number may contain only digits, hyphens, and an optional leading +.")
            return False

        if email and not self.validate_email(email):
            print("Error: Email must contain '@' and '.'.")
            return False

        if self.find_contact_by_name(name):
            print(f"Error: A contact with the name '{name}' already exists.")
            return False

        self.contacts.append({"name": name.strip(), "phone": phone.strip(), "email": email.strip() if email else ""})
        print(f"Contact '{name}' added successfully.")
        return True

    def find_contact_by_name(self, name: str) -> Optional[Dict[str, str]]:
        name_lower = name.strip().lower()
        return next((c for c in self.contacts if c["name"].lower() == name_lower), None)

    def view_contact(self, name: str) -> None:
        contact = self.find_contact_by_name(name)
        if not contact:
            print(f"Contact '{name}' not found.")
            return

        print(self.format_contacts([contact]))

    def update_contact(self, name: str, phone: Optional[str] = None, email: Optional[str] = None) -> bool:
        contact = self.find_contact_by_name(name)
        if not contact:
            print(f"Contact '{name}' not found.")
            return False

        if phone is not None and phone.strip():
            if not self.validate_phone(phone):
                print("Error: Phone number may contain only digits, hyphens, and an optional leading +.")
                return False
            contact["phone"] = phone.strip()

        if email is not None:
            if email.strip() and not self.validate_email(email):
                print("Error: Email must contain '@' and '.'.")
                return False
            contact["email"] = email.strip()

        print(f"Contact '{name}' updated successfully.")
        return True

    def delete_contact(self, name: str) -> bool:
        contact = self.find_contact_by_name(name)
        if not contact:
            print(f"Contact '{name}' not found.")
            return False

        self.contacts.remove(contact)
        print(f"Contact '{name}' deleted successfully.")
        return True

    def search_contacts(self, query: str) -> List[Dict[str, str]]:
        query_lower = query.strip().lower()
        if not query_lower:
            return []

        return [
            c
            for c in self.contacts
            if query_lower in c["name"].lower()
            or query_lower in c["phone"].lower()
            or query_lower in c.get("email", "").lower()
        ]

    def list_contacts(self) -> List[Dict[str, str]]:
        return list(self.contacts)


def prompt_for_optional_input(prompt_message: str) -> str:
    return input(prompt_message).strip()


def main() -> None:
    manager = ContactManager()

    while True:
        print("\n=== Contact Manager Menu ===")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Search Contacts")
        print("6. List All Contacts")
        print("7. Exit")
        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            name = input("Enter name: ").strip()
            phone = input("Enter phone: ").strip()
            email = prompt_for_optional_input("Enter email (optional): ")
            manager.add_contact(name, phone, email)

        elif choice == "2":
            name = input("Enter name to view: ").strip()
            manager.view_contact(name)

        elif choice == "3":
            name = input("Enter name to update: ").strip()
            if not manager.find_contact_by_name(name):
                print(f"Contact '{name}' not found.")
                continue

            phone = prompt_for_optional_input("Enter new phone (leave blank to keep current): ")
            email = prompt_for_optional_input("Enter new email (leave blank to keep current or clear email): ")
            if phone == "":
                phone = None
            if email == "":
                email = None
            manager.update_contact(name, phone=phone, email=email)

        elif choice == "4":
            name = input("Enter name to delete: ").strip()
            manager.delete_contact(name)

        elif choice == "5":
            query = input("Enter search term (name, phone, or email): ").strip()
            results = manager.search_contacts(query)
            print(manager.format_contacts(results))

        elif choice == "6":
            print(manager.format_contacts(manager.list_contacts()))

        elif choice == "7":
            print("Exiting Contact Manager. Goodbye!")
            break

        else:
            print("Invalid option. Please choose a number from 1 to 7.")


if __name__ == "__main__":
    main()
