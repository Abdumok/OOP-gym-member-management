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


