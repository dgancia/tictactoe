import os
import csv
import pwinput
import time
from login import login

is_exit = False
main_menu_input = ''

def main():
    clear()
    print(">","="*102,"<")
    print("|  __________   __   ________     __________   ________   ________     __________   ________   ________  |")
    print("| |___    ___| |  | /   _____|   |___    ___| |   __   | /   _____|   |___    ___| /   __   \ /   _____| |")
    print("|     |  |     |  | |  |             |  |     |  |  |  | |  |             |  |     |  |  |  | |  |____   |")
    print("|     |  |     |  | |  |             |  |     |  |__|  | |  |             |  |     |  |  |  | |   ____|  |")
    print("|     |  |     |  | |  |_____        |  |     |   __   | |  |_____        |  |     |  |__|  | |  |_____  |")
    print("|     |__|     |__| \________|       |__|     |__|  |__| \________|       |__|     \________/ \________| |")
    print("|","                                                                                                       |")

    print(">","="*102,"<")
    print("|",'                                          [1] Register' ,"                                                |")
    print("|",'                                          [2] Login' ,"                                                   |")
    print("|",'                                          [3] Logout' ,"                                                  |")
    print("|",'                                          [4] Reset Password' ,"                                          |")
    print(">","="*102,"<")
    global main_menu_input
    main_menu_input = input('==> Choice: ')
    is_exit = False

    while is_exit == False:
        if main_menu_input == '1':
            clear()
            register()
            main()
        if main_menu_input == '2':
            clear()
            login()
        if main_menu_input == '3':
            clear()
            logout()
            main()
        if main_menu_input == '4':
            clear()
            reset_password()
            main()
        
        return True

def register():
    print(">","="*102,"<")
    print('|                                          REGISTRATION FORM                                             |')
    print(">","="*102,"<")
    username = input('|                                      Enter your username: ')
    password = pwinput.pwinput(prompt='|                                       Enter your password: ', mask='*')
    print(">","="*102,"<")
    enterr = input("==> Press Enter to Continue...")
    with open('database.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([username, password])
    return True

def logout():
    return True

def reset_password():
    print(">","="*102,"<")
    print('|                                          RESET PASSWORD FORM                                           |')
    print('|                                              Login First                                               |')
    print(">","="*102,"<")
    username = input('|                                      Enter your username: ')
    password = pwinput.pwinput(prompt='|                                       Enter your password: ', mask='*')
    with open('database.csv') as csv_file:
        reader = csv.reader(csv_file)
        is_success = False
        counter = 0
        index = None
        new_list = []
        for row in reader:
            new_list.append(row)
            if len(row) > 1:
                if row[0] == username and row[1] == password:
                    is_success = True
                    index = counter
            counter += 1
        
        if is_success:
            print(">","="*102,"<")
            new_password = input('|                                       Input New Password: ')
            print(">","="*102,"<")
            enterr = input("==> Press Enter to Continue...")
            for i in range(len(new_list)):
                if i == index:
                    new_list[i][1] = new_password
            with open('database.csv', 'w+') as csv_file:
                writer = csv.writer(csv_file)
                for i in range(len(new_list)):
                    writer.writerow(new_list[i])
            time.sleep(20)
        else:
            print('Login Failed')
        global is_exit
        global main_menu_input
        is_exit = True
        main_menu_input = ''
        # time.sleep(10)

def clear():
    os.system('clear||cls')

main()