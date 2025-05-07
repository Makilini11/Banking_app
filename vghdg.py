def get_customer_info():
    user_name=input("Enter the username:")
    password=input("enter the password:")
    name = input('Enter the name:')
    address = input("Enter the Address:")
    phone_number=(input("Enter the phonenumber:"))
    email=input("Enter the email:")

    file = open('login.txt','w')
    file.write(f'{user_name}:{password}:{name}:{address}:{phone_number},{email}\n')
    file.close()
get_customer_info()