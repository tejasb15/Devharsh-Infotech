import pandas as pd
import os

file_path = 'users_data.xlsx'

def add_user():
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone Number: ")

    new_user = pd.DataFrame({
        'Name':[name],
        'Email':[email],
        'Phone Number':[phone]
    })

    if os.path.exists(file_path):
        existing_data = pd.read_excel(file_path)
        updated_data = pd.concat([existing_data, new_user], ignore_index=True)
    else:
        updated_data = new_user

    updated_data.to_excel(file_path, index=False)
    print("User added successfully!\n")

def display_users():
    if os.path.exists(file_path):
        users_data = pd.read_excel(file_path)
        if users_data.empty:
            print("No users found.\n")
        else:
            print("\nStored Users:")
            print(users_data.to_string(index=False), "\n")
    else:
        print("No users found.\n")



def main():
    while True:
        print("1. Add User")
        print("2. Display Users")
        print("3. Exit")

        choice = input("Enter Your Choice : ")

        if choice == '1':
            add_user()
        elif choice == '2':
            display_users()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":

    main()