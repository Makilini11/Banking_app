#admin login

# def read_file():
#     user_name="Admin"
#     pass_word="12345"
#     file=open('login.txt','a')
#     file.write(f"Enter Admin User Name Is:"{user_name})
#     file.write(f"Enter Admin Password Is:"{pass_word})


# def Admin_login():
#     try:
#         print("====Admin Login====")
#         Admin_username=input("")
#         Admin_userpassword=int(input("Enter Admin User Password Is:" ))
#         if Admin_username==user_name and Admin_userpassword==user_password:
#             print("Login Successfully!")
#             print("🙏Welcome to MK Bank🙏")
#         else:
#             print("🚫Invalid login🚫.Try Again.")
#     except ValueError:
#         print("Enter Valid Number")
# Admin_login()
def get_customer_info():
    user_name=input("Enter the username: ")
    password=input("Enter the password: ")
    name = input('Enter the name:')
    date_of_birth = ("Enter the date of birth: ")
    address = input("Enter the Address: ")
    phone_number=(input("Enter the phonenumber: "))
    email=input("Enter the email: ")
    return [name, address, phone_number, email, user_name, password]
def create_customers_and_users():  
    customers=get_customer_info()
    with open("customers.txt","a") as customer_file, open("users.txt","a") as user_file:
        customer_file.write(f"{customers[2]},{customers[3]}")
        user_file.write(f"{customers[0]},{customers[1]}")
create_customers_and_users()
#admin menu
def Admin_menu():
    while True:
        print("1. Create Customer")
        # print("2. Create Account")
        # print("3. Deposit Money")
        # print("4. Withdraw Money")
        # print("5. Check Balance")
        # print("6. View Transaction History")
        # print("7. view All Account")
        # print("8. Delete Account ")
        # print("9. Update Account Details")
        print("10. exit")
        choice=input("Enter the choice(1-10):") 
        if choice==1:
            print(create_customers_and_users)
        # elif choice==2:
        #     print(create_account)
        # elif choice==3:
        #     print(deposit_money)
        # elif choice==4:
        #     print(withdraw_money)
        # elif choice==5:
        #     print(check_balance)
        # elif choice==6:
        #     print(view_transaction_history)
        # elif choice==7:
        #     print(view_all_accounts)
        # elif choice==8:
        #     print(delete_accounts)
        # elif choice==9:
        #     print(update_account_details)
        elif choice==10:
            print(exit)
Admin_menu()       



            





