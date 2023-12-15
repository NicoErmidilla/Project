EMERGENCY = {"BFP" : "425-7163/301-7996/ 09156021984",
            "PNP" : "723-2030"}
HOSPITAL = {"BATMC" : "723-0911",
                  "ST. PATRICKS" : "723-1605",
                  "NAZARETH" : "723-4144",
                  "GOLDEN GATE" : "723-2508"}
DEPRESSION = {"NCMH CRISIS HOTLINES":"1553\ 0966-351-4518(GLOBE)\ 0908-639-2627(SMART)",
                    "IN TOUCH CS CRISIS LINES" : "(02)8893-7603\0917-800-1123(GLOBE)\0922-893-8944(SUN)",
                    "MANILA LIFELINE CENTRE" : "(02)896-9191\0917-854-9191"}                          
NEW ={}

def display_emergency():
    print("\t\t\t\t\tFor Emergency \n")
    print("Name\t\t\t\t\tContact Number")
    for key in EMERGENCY:
        print("{}\t\t\t\t{}\n".format(key, EMERGENCY.get(key)))

def display_hospital():
    print("\t\t\t\t\tFor Hospital hotlines\n")
    print("Name\t\t\t\t\t\tContact Number")
    for key in HOSPITAL:
        print("{}\t\t\t\t{}\n".format(key, HOSPITAL.get(key)))

def display_depression():
    print("\t\t\t\tFor Depression hotlines\n")
    print("Name\t\t\t\t\t\tContact Number")
    for key in DEPRESSION:
        print("{}\t\t{}\n".format(key, DEPRESSION.get(key)))

def display_new():
    print("\t\t\t\tFor Yor Added hotlines\n")
    print("Name\t\t\t\t\t\tContact Number")
    for key in NEW:
        print("{}\t\t{}\n".format(key, NEW.get(key)))





while True:
    choice = int(input(" 1. Add new hotline \n 2. Search hotline \n 3. Display hotline \n 4. Edit hotline \n 5.Delete hotline \n 6. Exit \n Enter your choice: "))
    if choice  == 1:
        name = input("Enter the hotline name: " ).upper()
        phone = input("Enter the hotline number: " )
        NEW[name] = phone
    elif choice == 2:
        search_name = input("Enter the hotline name: " ).upper()
        if search_name in EMERGENCY:
            print(search_name, " 's hotline number is ", EMERGENCY[search_name])
        elif   search_name in HOSPITAL:
            print(search_name, " 's hotline is ", HOSPITAL[search_name]) 
        elif   search_name in DEPRESSION:
            print(search_name, " 's hotline is ", DEPRESSION[search_name]) 
        elif   search_name in NEW:
            print(search_name, " 's hotline number is ", NEW[search_name])     
        else:
            print(" Name is not found in hotline ") 
    elif choice == 3:
        display_emergency()
        display_hospital() 
        display_depression()
        display_new()

    elif choice == 4:
        edit_contact = input("Enter the hotline to be edited: ").upper()
        if edit_contact in EMERGENCY:
            phone = input("Enter the number: ")
            EMERGENCY[edit_contact] = phone
            print("hotline updated!")  
            display_emergency ()
        elif edit_contact in HOSPITAL:
            phone = input("Enter the number: ")
            HOSPITAL[edit_contact] = phone
            print("hotline updated!")  
            display_hospital ()
        elif edit_contact in DEPRESSION:
            phone = input("Enter the number: ")
            DeprecationWarning[edit_contact] = phone
            print("hotline updated!")  
            display_depression ()
        elif edit_contact in NEW:
            phone = input("Enter the number: ")
            DeprecationWarning[edit_contact] = phone
            print("hotline updated!") 
        
        
        else:
            print("Name is not found in the hotline collection")
    elif choice == 5:
        del_contact = input("Enter the hotline to be deleted: ").upper()
        if del_contact in EMERGENCY:
            confirm = input("Do you want to delete this hotline Y/N?").upper()
            if confirm == 'Y' :
                EMERGENCY.pop(del_contact) 
            display_emergency()
        elif del_contact in HOSPITAL:
            confirm = input("Do you want to delete this contact y/n?").upper()
            if confirm == 'y' or confirm == 'Y' :
                HOSPITAL.pop(del_contact)
            display_hospital()        
        elif del_contact in DEPRESSION:
            confirm = input("Do you want to delete this contact y/n?").upper()
            if confirm == 'y' or confirm == 'Y' :
                DEPRESSION.pop(del_contact) 
            display_depression()
        elif del_contact in NEW:
            confirm = input("Do you want to delete this contact y/n?").upper()
            if confirm == 'y' or confirm == 'Y' :
                NEW.pop(del_contact)
            display_new()
        else: 
           
            print("Name is not found in contact book")
            display_emergency()
            display_hospital()
            display_depression()
            display_new()

   
    else: 
        break