class ContactFunctionality:

    def __init__(self, add, delete, change, contact_list, contact, instruction ):
        self.add = add
        self.delete = delete
        self.change = change
        self.contact_list = contact_list
        self.contact = contact
        self.user_instruction = instruction

    def add_contact(self):
        instruction = input("would you like to add, delete or change a contact")

        while instruction == "yes":
            self.contact_list = []
            self.contact = {}
            self.contact["First Name"] = input("Please enter the first name")
            self.contact["Last Name"] = input("Please enter the last name")
            self.contact["Cell Number"] = input("Please enter the cell number")
            self.contact["Email "] = input("Please enter the email")
            self.contact_list.append(self.contact)
            instruction = input("Would you like to add another contact? ").lower()



