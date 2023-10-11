#   Create a program witch takes 5 different (minmum)  variables containing strings for username and password.
# The string should look like : "username='', password=''; username='',password='';....etc"
# Start Endless loop allowing to enter username and password and 
# check ff credentials are correct stop endless loop and print greeting message, otherwise print 'wrong credentials'
# and ask to enter password and username again. The program should show numbers of times you tried to enter both credentials.

# print("Enter five different username and password")
# name_and_pasvord =input ("username1=": "password1","username2=": "password2","username3=": "password3","username4=": "password4","username5=": "password5")
# print(name_and_pasvord)





user_name_list = []
user_password_list = []

print("Enter five different username and password")

for add in range(5):
    username = input("Add username: ")
    password = input("Add password: ")
    user_name_list.append(f"username='{username}'")
    user_password_list.append(f"password='{password}'")

while True:
    username_input = input("Enter username: ")
    password_input = input("Enter password: ")

    if f"username='{username_input}'" in user_name_list and f"password='{password_input}'" in user_password_list:
        print("Welcome")
        break
    else:
        print("Wrong password. Please try again.")

        

    

    

