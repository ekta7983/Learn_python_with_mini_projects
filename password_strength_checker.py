password = input("Enter your password:")

if(len(password) < 6):
    print("Please enter a password with at least 6 characters.")
elif (len(password)>=6 and len(password)<=10):
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special_character = False

    for c in password:
        if(c.isupper()):
            has_uppercase = True
        elif(c.islower()):
            has_lowercase = True
        elif c.isdigit():
            has_digit = True
        elif c in "!@#$%^&*":
            has_special_character = True
        else:
            print("Password contains invalid character: " + c)
            break
    if has_uppercase and has_lowercase and has_digit and has_special_character:
        print("Your password is strong.")
    else:
        if not has_uppercase or not has_lowercase:
            print("Password must contain both uppercase and lowercase letters.")
        if not has_digit:
            print("Password must contain at least one digit.")
        if not has_special_character:
            print("Password must contain at least one special character (!@#$%^&*).")

        print("your password is weak.")
else:
    print("Please enter a password with no more than 10 characters.")
