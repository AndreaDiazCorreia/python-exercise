email = input("Enter your email: ")

if len(email) >= 6:
    if email[0].isalpha():
        if "@" in email and email.count("@") == 1:
            if (email[-4] == "." or email[-3] == "."):
                k = j = d = 0  
                for i in email:
                    if i.isspace():
                        k = 1
                    elif i.isalpha():
                        if i.isupper():
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i == "_" or i == "." or i == "@":
                        continue
                    else:
                        d = 1
                if k == 1 or j == 1 or d == 1:
                    print("Invalid Email")
                else:
                    print("Valid Email")
            else:
                print("Invalid Email")
        else:
            print("Invalid Email")
    else:
        print("Invalid Email")
else:
    print("Invalid Email")