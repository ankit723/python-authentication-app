def user_input():
    username = input("Enter Username: ")
    password = input("Enter New Password: ")
    return username, password

def sign_up(username, password):
    db = open("database.txt", "r")
    d = []
    f = []
    for i in db:
        a,b = i.split(", ")
        b = b.strip()
        d.append(a)
        f.append(b)
    data = dict(zip(d, f))
    if username in d:
        print("Username already exists")
        exit()
    else:
        with open("database.txt", "a") as db:
            db.write(username + ", " + password + "\n")
            db.close()
            print("Account Created Succesfully")
            return

 

sign_up(*user_input())