"""
Netti Welsh
Fall 2020 CS5001
Problem 2: Password
"""

def secure_password(password):
    types = 0
    # no main() for this problem
    # must be between 9 and 12 chars long
    valid_length = len(password) >= 9 and len(password) <=12
    # and must meet at least 3 req
       # 1. at least one lowercase
    contains_lower = any(i.islower() for i in password)
       #print(contains_lower)
       # 2. at least one uppercase
    contains_upper = any(i.isupper() for i in password)
       #print(contains_upper)
       # 3. at leat one digit (0-9)
    contains_digit = any(i.isdigit() for i in password)
       #print(contains_digit)
       # 4. at least 1 of the following chars($,#,@,!)
    if valid_length == False:
        return False
    else:
        if contains_lower == True:
            types+= 1
            print(types)
        if contains_upper == True:
            types+=1
            print(types)
        if contains_digit == True:
            types+=1
            print(types)
        if valid_special_chars(password) == True:
            types+=1
            print(types)

        return True if types >= 3 else False
        #if types >=3:
        #    return True
         #   else:
            #    return False


def special_characters_check(password):
    pass

def valid_special_chars(password):
    permitted_chars = ['$', '#','@','!']
    used_chars = []
    #contains_permitted_chars = True for i in password if i in permitted_chars]
    for i in password:
        if i in permitted_chars:
            used_chars.append(i)
    if len(used_chars)==0:
        return False
    else:
        return True

    #return (used_chars)
        #print(contains_permitted_chars)
    # It should not contain other special chars then($, #,@,!)

#print(valid_special_chars(password))


def main():

    password = input("Enter password: ")

    print(secure_password(password))
    #print(valid_special_chars(password))

if __name__ == "__main__":
    main()