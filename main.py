from contact import Contact
print("Welcome to your contact list.")
contact = Contact()

active_contact_list = True

while active_contact_list:
    user_input = (input("Would you like to Add or Delete Contact? please choose (Add or Delete): Enter stop to exit ")
                  .lower())

    if user_input == "add":
        contact.new_contact()
    elif user_input == "delete":
        contact.delete_contact()
    elif user_input == "change":
        contact.change_contact()

    else:

         if user_input == "stop":
            active_contact_list = False
            print(contact.contact_list)
            print("The contact list app is now closed")





