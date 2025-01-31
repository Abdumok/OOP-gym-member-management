import os
from re import search


def clear():
    os.system("cls" if os.name == "nt" else "clear")

members = []

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
        last_name = input("Enter your last name: ")
        membership_id = input("Enter Membership id: ")
        status = input("Enter membership status (active, inactive), or press enter: " )
        if status == "active":
            status = "active"
        else:
            status = "inactive"

        return Membership(first_name, last_name, membership_id, status)

    @staticmethod
    def add_member():
        members.append(Membership.new_member())
        print("Member was add successfully")

    @staticmethod
    def search(member_list):
        clear()
        print("\nSearch by:")
        print("1. Membership")
        print("2. First name")
        print("3. Membership Status")

        choice = input("Enter your choice: ")
        member_found = []

        if members:

            if choice == "1":
                member_id = input("\nEnter membership ID: ")
                for member in member_list:
                    if member.membership_id == member_id:
                        member_found.append(member)
                    else:
                        pass
            elif choice == "2":
                first_name = input("\nEnter the first name: ")
                for member in member_list:
                    if member.f_name.lower() == first_name.lower():
                        member_found.append(member)
                    else:
                        pass
            elif choice == "3":
                stat = input("\nEnter the status: ")
                for member in member_list:
                    if member.status.lower() == stat.lower():
                        member_found.append(member)
                    else:
                        pass
            else:
                print("Invalid input, Try again")
                Membership.search(member_list)
            if member_found:
                print("Members found")
                for member in member_found:
                    Membership.member_info(member)
            else:
                print("No member found")



# program logic:
system_on = True
while system_on:
    clear()
    Membership.menu()

    # Ask user to choose form menu
    choice = input("what is your choice: ")

    if choice == "1":
        Membership.add_member()
        input("\nPress enter to return to the main menu")

    elif choice == "2":
        if members:
            for member in members:
                Membership.member_info(member)
        else:
            print("There not members to display")
        input("\nPress enter to return to the main menu")

    elif choice == "3":
        if members:
            Membership.search(members)
        else:
            print("\nSorry there is no members to display")

        if input("Do you want to search for another member: (Y/N) ").lower() == "y":
            Membership.search(members)
        else:
            pass
    elif choice == "4":
        system_on = False
    else:
        print("Invalid input, Try again")





