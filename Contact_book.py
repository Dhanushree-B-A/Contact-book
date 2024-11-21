contact = {}
def display_contact():
   print("Name\t\tContact Number")
   for key in contact:
      print("{}\t\t{}".format(key,contact.get(key)))

while True:
   choice = int(input("1. Add contact\n2. Search contact\n3. Display contact\n4. Edit contact\n5. Delete contact\n6. Exit\n"))
   if(choice == 1):
      name = input("Enter the contact name: ")
      phone = input("Enter the mobile number: ")
      contact[name] = phone
      print("Contact is added to the contact book")
   elif(choice == 2):
      search_name = input("Enter the name to serach: ")
      if(search_name in contact):
         print(search_name, "s contact number is ", contact[search_name])
      else:
         print("Name is not found in contact book")
   elif(choice == 3):
      if(not contact):
         print("Empty contact book")
      else:
         display_contact()
   elif(choice == 4):
      edit_contact = input("Enter the contact to be edited: ")
      if(edit_contact in contact):
         phone = input("Enter mobile number: ")
         contact[edit_contact] = phone
         print("Contact updated!")
         display_contact()
      else:
         print("Name is not found in contact book")
   elif(choice == 5):
      del_contact = input("Enter the contact to be deleted: ")
      if(del_contact in contact):
         confirm = input("Do you want to delete this contact? ")
         if(confirm == 'y' or confirm == 'Y'):
            contact.pop(del_contact)
         display_contact()
      else:
         print("Name is not found in contact book")
   else:
      break


      
