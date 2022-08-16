

def main():
    name_to_email = {}
    email = get_email()
    while email != "":
        name = get_name_from_email(email)
        validation = input(f'Is your name {name}? (Y / N)').upper()
        while validation == "":
            print("Please enter y or n")
            validation = input(f'Is your name {name}? (Y / N)').upper()
        if validation != "Y" and validation != "":
            name = input("Name: ")
        # print(email)
        name_to_email[email] = name
        # print(name)
        # print(name_to_email)
        email = get_email()

    for email, name in name_to_email.items():
        print(f"{name} ({email})")




def get_email():
    """Gets email from user input"""
    email = input("Email: ")
    return email

def get_name_from_email(email):
    """Takes name from the email address"""
    user = email.split("@")[0]
    parts = user.split(".")
    name = " ".join(parts).title()
    return name

main()
