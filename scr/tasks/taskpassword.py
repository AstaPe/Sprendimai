from scr.classes.passwordvalidator import PasswordValidator

password = "Password123"
validator = PasswordValidator(password)

if validator.is_valid():
    print(f'The password "{password}" is valid.')
else:
    print(f'The password "{password}" is not valid.')