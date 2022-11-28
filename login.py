import pwinput
import csv



def login():
    print(">","="*102,"<")
    print('|                                                LOGIN FORM                                              |')
    print(">","="*102,"<")
    username = input('|                                        Enter your username: ')
    password = pwinput.pwinput(prompt='|                                            Password: ', mask='*')
    print(">","="*102,"<")
    enterr = input("Press Enter to Continue...")
    with open('database.csv') as csv_file:
        reader = csv.reader(csv_file)
        is_success = False
        for row in reader:
            if len(row) > 1:
                if row[0] == username and row[1] == password:
                    is_success = True
        
        if is_success:
            
            print('Login Success')
            import tictactoe
            tictactoe()

        else:
            print('Login Failed')
        global is_exit
        global main_menu_input
        is_exit = True
        main_menu_input = ''
        # time.sleep(10)