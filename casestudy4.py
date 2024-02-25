import csv # (comma separated values) file

# function for user registration
def register():
    print("Register:")
    name = input("Enter your name: ")
    address = input("Enter your address: ")
    phone = input("Enter your phone number: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    with open('users.csv', mode='a') as user_file:
        writer = csv.writer(user_file)
        writer.writerow([username, password, name, address, phone])
    print("Registration Successful.")
    print("Your UserID is:", username)
    print("Your Password is:", password)

# function for user login
def login():
    print("Login:")
    username = input("Enter username: ")
    password = input("Enter password: ")
    with open('users.csv', mode='r') as user_file:
        reader = csv.reader(user_file)
        for row in reader:
            if row[0] == username and row[1] == password:
                print("Welcome,", row[2])
                return
            else:
                print("Invalid Authentication.")

# function for searching product details
def search():
    print("Search a product Details:")
    print("Categories:")
    print("1. Men")
    print("2. Women")
    print("3. Kids")
    category = int(input("Enter category number: "))
    if category == 1:
        print("Cloth Types:")
        print("1. T-shirt - Rs. 500")
        print("2. Jeans - Rs. 1000")
        print("3. Shirts - Rs. 800")
        print("4. Kurta sets - Rs. 1500")
    elif category == 2:
        print("Cloth Types:")
        print("1. Kurti sets - Rs. 2000")
        print("2. Tops and tees - Rs. 1000")
        print("3. Sarees - Rs. 3000")
        print("4. Jeans - Rs. 1500")
        print("5. Westerns - Rs. 2500")
    elif category == 3:
        print("Cloth Types:")
        print("1. Shirts - Rs. 600")
        print("2. Night suits - Rs. 1000")
        print("3. Frocks - Rs. 800")
        print("4. Joggers - Rs. 700")

# function for buying clothes
def buy():
    print("Buying Clothes:")
    quantity = int(input("Enter quantity: "))
    size = input("Enter size: ")
    address = input("Enter customer address: ")
    print("Product added to bill.")

# function for bill generation
def bill():
    print("Bill Generation:")
    date = input("Enter date of purchase: ")
    username = input("Enter user ID: ")
    time = input("Enter time: ")
    phone = input("Enter phone number: ")
    bill_no = input("Enter bill number: ")
    print("Thank you for shopping with us.")



while True:
    print("1. Register")
    print("2. Login")
    print("3. Search a product")
    print("4. Buy Clothes")
    print("5. Generate Bill")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        register()
    elif choice == 2:
        login()
    elif choice == 3:
        search()
    elif choice == 4:
        buy()
    elif choice == 5:
        bill()
    elif choice == 6:
        exit()
    else:
        print("Invalid choice")