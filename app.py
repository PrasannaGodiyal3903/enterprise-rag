from users import users

def login(username, password):
    if username in users:
        if users[username]["password"] == password:
            return users[username]["role"]
    return None
  
username = input("Username: ")
password = input("Password: ")

role = login(username, password)

if role:
    print(f"Login successful. Role: {role}")
else:
    print("Invalid credentials")
