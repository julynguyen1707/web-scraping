# from sub_module import func1


# print("Welcome to my program")
# func1()


#Practice 2:
from sub_module import emailProcess, printMessage

def main():
    emails = ["trannguyen1707@yahoo.com","julynguyen.dev@gmail.com","tran.nguyen.backup@gmail.com","tran.n@company.com"
            "tnguyen@company.com","tran.nguyen.analytics@company.com"]
    for email in emails:
            email_username, email_domain = emailProcess(email)
            printMessage ( email_username, email_domain)


if __name__ == "__main__":
    main()