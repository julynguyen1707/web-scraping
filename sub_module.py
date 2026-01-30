# def welcome():
#     print("Welcome to CodeXplore Channel")

# def func1():
#     print("This is func1")

# def main():
#     welcome()
#     func1()


# Practice 2:

def emailProcess(email):
    #example: youtube@gmail.com
    email_username = email[0:email.index("@")]
    email_domain = email[email.index("@")+1:]
    #print(f"Username is {email_username}")
    return [email_username, email_domain]

def printMessage(email_username, email_domain):
    print(f"Username is {email_username}; Email Domain is {email_domain}")

def main():
    email = input("Please enter your email: ").strip()
    email_username, email_domain = emailProcess(email)
    printMessage(email_username, email_domain)
    
# main()

## because when you import sub_module it will include whole rows. in order to run the formula you want, you need to add 
# if __name__ = __main__
#      main()
if __name__ == "__main__":
    main()