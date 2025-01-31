import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

class Membership:
    def __init__(self, first_name, last_name, membership_id, status = "inactive"):
        self.f_name = first_name
        self.l_name = last_name
        self.membership_id = membership_id
        self.status = status

    def member_info(self):
        print(f"\nFirst name: {self.f_name}")
        print(f"last name: {self.l_name}")
        print(f"Membership ID: {self.membership_id}")
        print(f"Status: {self.status}")
        print("----------------------------------")

    # main menu
    @staticmethod
    def menu():
        print("Welcome to GYM Membership Management\n")
        print("1. Add new member")
        print("2. Display all members")
        print("3. Search for a member")
        print("4. Exit")

    @staticmethod
    def new_member():
        first_name = input("\nEnter your first name: ")
        last_name = input("\nEnter your last name: ")
        membership_id = input("\nEnter Membership id: ")
        status = input("\nEnter membership status (active, inactive), or press enter: " )
        if status == "active":
            status = "active"
        else:
            status = "inactive"

            return Membership(first_name, last_name, membership_id, status)


