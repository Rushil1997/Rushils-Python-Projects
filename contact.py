
class Contact:
    def __init__(self):
        self.contact_list = []
        self.contact = {}


    def new_contact(self):
        name = input("Enter the Name of the Contact: ")
        cell_number = input("Enter the Cell Number of the Contact: ")
        e_mail = input("Enter the E-mail of the Contact: ")

        self.contact = {
            "Name": name,
            'Cell Number': cell_number,
            "E-mail": e_mail,
        }
        self.contact_list.append(self.contact)

    def delete_contact(self):
        print(self.contact_list)
        delete_contact = int(input("Which contact would you like to delete? (please choose a number that represents a "
                                   "contact): "))
        self.contact_list.pop(delete_contact - 1)
        print(self.contact_list)

 
