import os

def user_input():
    username = input("Enter your existing username: ")
    password = input("Enter your existing password: ")
    return username, password

def reset_password(username):
    new_password = input("Enter your new password: ")
    db = open("database.txt", "r")
    d = []
    f = []
    for i in db:
        a,b = i.split(", ")
        b = b.strip()
        d.append(a)
        f.append(b)
    data = dict(zip(d, f))
    data[username] = new_password
    db.close()
    db = open("database.txt", "w")
    for i in data:
        db.write(i + ", " + data[i] + "\n")
    db.close()
    print("Your password has been reset")
    os.system("python3 sign_in.py")

def sign_in(username, password):
    db = open("database.txt", "r")
    if not len(username or password)<1:
        d = []
        f = []
        for i in db:
            a,b = i.split(", ")
            b = b.strip()
            a = a.strip()
            d.append(a)
            f.append(b)
        data = dict(zip(d, f))
        
        try:
            
            if password == data[username]:
                print("Welcome back, {}!".format(username))
                login = True
                print("Login successful")
                if login == True:
                    os.startfile("test2.py")

            else:
                print("Incorrect password! try again")
                reset = input("Do you wnat to reset your password? (y/n)")
                if reset == "y":
                    reset_password(username)
                elif reset == "n":
                    try_again = input("do you want to try agin? (y/n)")
                    if try_again == "y":
                        username, password = user_input()
                        sign_in(username, password)
                    elif try_again == "n":
                        print("Goodbye")
                        exit()
                    else:
                        print("Invalid input")
                        exit()
                else:
                    print("Invalid input")
                    exit()
        except KeyError:
            print("Invalid username")
            exit()
       

    else:
        print("provide a username and password! try again")
        sign_in(username, password)

