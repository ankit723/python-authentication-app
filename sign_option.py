import os

while True:
    print("Do you want to sign in or sign up?")
    print("1. Sign in")
    print("2. Sign up")

    input_option = input("Enter your option: ")
    if input_option == "1":
        print("Sign in")
        os.startfile("C:\\Users\\studi\Desktop\\python learn\\sign_in.py")
    elif input_option == "2":
        print("Sign up")
        os.startfile("C:\\Users\\studi\Desktop\\python learn\\sign_up.py")
    else:
        print("Invalid option")

        
