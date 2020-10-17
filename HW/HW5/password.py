"""
Netti Welsh
Fall 2020 CS5001
Problem 2: Password
"""

def secure_password(password):
    # no main() for this problem
    # must be between 9 and 12 chars long
    if len(password) >= 9 and len(password) <=12:


    # and must meet at least 3 req
       # 1. at least one lowercase
       contains_lower = any(i.islower() for i in password)
       print(contains_lower)
       # 2. at least one uppercase
       contains_upper = any(i.isupper() for i in password)
       print(contains_upper)
       # 3. at leat one digit (0-9)
       contains_digit = any(i.isdigit() for i in password)
       print(contains_digit)
       # 4. at least 1 of the following chars($,#,@,!)
def valid_special_chars(password):

        permitted_chars = ['$', '#','@','!']

       #contains_permitted_chars = True for i in password if i in permitted_chars]
        for i in password:
            if i in permitted_chars:
                print("True")
            else:
                print("False")

        #print(contains_permitted_chars)
    # It should not contain other special chars then($, #,@,!)



def main():
    password = input("Enter password: ")
    print(secure_password(password))
    print(valid_special_chars(password))

if __name__ == "__main__":
    main()