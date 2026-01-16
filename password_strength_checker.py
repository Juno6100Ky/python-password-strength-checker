import getpass

def check_password_strength(password):
    errors = []
    specials = """~!@#$%^&*()_+-=[]{}\|"'<>,./? ;:"""
    has_number = False
    has_upper = False
    has_lower = False
    has_special = False

    if len(password) < 8:
        return "Weak: Too short (must be 8+ characters)"
    
    for char in password:
        if char.isdigit():
            has_number = True
        
        elif char.isupper():
            has_upper = True

        elif char.islower():
            has_lower = True

        elif char in specials:
            has_special = True 

    if has_number and has_upper and has_lower and has_special:
        return "Strong Password! Good job."
    
    if has_number is False:
        errors.append("Missing number")
    
    if has_upper is False:
        errors.append("Missing uppercase letter")

    if has_lower is False:
        errors.append("Missing lowercase letter")
    if has_special is False:
        errors.append("Missing special letter")
    return errors
    
    
while True:
    user_input = getpass.getpass("Enter a password to check: ")
    result = check_password_strength(user_input)
    if result == "Strong Password! Good job.":
        print(result)
        break
    else:
        print("Your password is weak:")
    print(result)