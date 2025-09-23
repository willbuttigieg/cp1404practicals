password_length_requirement = 8
password = str(input("Enter the password: "))
while len(password) < password_length_requirement:
    print(f"Password must be at least {password_length_requirement} characters long")
    password = str(input("Enter the password: "))
print("*" * len(password))

