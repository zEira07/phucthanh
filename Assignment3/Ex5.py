correct_username = "python"
correct_password = "rules"

attempts = 0

while attempts < 5:
    username = input("Username: ")
    password = input("Password: ")

    if username == correct_username and password == correct_password:
        print("Welcome")
        attempts = 5   # kết thúc vòng lặp
    else:
        attempts += 1

if username != correct_username or password != correct_password:
    print("Access denied")
