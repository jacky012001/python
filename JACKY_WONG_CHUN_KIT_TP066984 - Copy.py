#JACKY WONG CHUN KIT
#TP066984
##############################################################
#REFER LINE FOR FUNCTION                                     #
#LINE 29 - 49   ---> MAIN HOMEPAGE                           #
#LINE 52 - 74   ---> INITIAL INVENTORY CONFIRMATION PAGE     #
#LINE 77 - 194  ---> INITIAL INVENTORY CREATION PAGE         #
#LINE 197 - 223 ---> MAIN MENU PAGE                          #
#LINE 226 - 254 ---> UPDATE ITEM INVENTORY PAGE              #
#LINE 257 - 323 ---> INCREASE ITEM INVENTORY PAGE            #
#LINE 326 - 414 ---> DECREASE ITEM INVENTORY PAGE            #
#LINE 421 - 489 ---> UPDATE SUPPLIER PAGE                    #
#LINE 496 - 502 ---> UPDATE HOSPITAL DETAIL PAGE             #
#LINE 505 - 573 ---> UPDATE DETAIL PAGE                      #
#LINE 576 - 634 ---> CREATE DETAIL PAGE                      #
#LINE 637 - 692 ---> TRACK ITEM PAGE                         #
#LINE 695 - 742 ---> SEARCH ITEM PAGE                        #
##############################################################
#Import time function
from datetime import datetime

#Import re as regular expression for validation of user input
import re

#Import os path for validation of file existance
import os.path

#Main homepage of PPE system
def Start_Up_Page():
    print("This program is created by:")
    print("Student Name : JACKY WONG CHUN KIT")
    print("TP Number    : TP066984")
    print()
    while True:
        print("*****WELCOME TO INVENTORY MANAGEMENT SYSTEM FOR PERSONAL PROTECTIVE EQUIPMENT(PPE)*****")
        print("---------------------------------------------------------------------------------------")
        print("Please login your account!")
        username = input("Username: ")  #Input username for accessing to the system
        password = input("Password: ")  #Input password for accessing to the system
        if ((username == "admin") and (password == "abc123")):  #ONLY username and password allowed
            print("LOGIN SUCCESS!")
            First_Creation_Confirm_Page()   #Enter initial inventory confirmation page
            break
        elif ((username == "") and (password == "")):
            print("Thank you for using this program! See you!") #Program will be terminated if both input empty
            break
        else:
            print("INVALID Username or Password! Please login again!")  #Have to input again if invalid
            print()

#Initial Inventory Confirmation Page
def First_Creation_Confirm_Page():
    print()
    print("*****WELCOME ADMIN! IS THIS THE FIRST TIME PROGRAM EXECUTED?*****")  #Ask whether is the program first time executed
    print("-----------------------------------------------------------------")
    print("    [A]  Yes\n    [B]  No\n   [ANY] Exit")  #Ask choice
    option = input()
    option = option.upper() #input a or b also acceptable
    if (option == "A"):
        if os.path.isfile("ppe.txt"):
            print("File already exist! Please proceed to Menu Page!")
            First_Creation_Confirm_Page()   #Back to Confirm Page if option A but file already exist
        else:
            First_Creation_Page()   #Enter Inventory Creation Page if option A and file doesn't exist
    elif (option == "B"):
        if os.path.isfile("ppe.txt"):
            Main_Menu_Page()    #Enter Main Menu Page if option B and file already exist
        else:
            print("No existing data! Please create initial inventory!")
            First_Creation_Confirm_Page()   #Back to Confirm Page if option B but file doesn't exist
    else:
        print("Proceeding to Start Up Page...")
        print()
        Start_Up_Page() #Enter back Main Homepage if any input key

#Initial Inventory Creation Page
def First_Creation_Page():
    print()
    print("Creating Initial Inventory...")
    print("Please enter your item name, item code, supplier code and stock quantity accordingly.")
    itemlist = []   #create empty list for itemlist after every user input
    total_item = [] #create empty list for total items after every user input
    pattern_1 = "[a-zA-Z]" #pattern for item_name, item_code input
    pattern_2 = "[a-zA-Z][a-zA-Z][0-9][0-9]"  #pattern for supplier_code input
    pattern_3 = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net)" #pattern for supplier_email input
    while True:
        while True:
            item_name = input("Enter Item Name: ")  #user need to input item name
            if (re.search(pattern_1,item_name)):    #break loop if pattern matches with input
                break
            else:
                print("Wrong format. Please try again.")
        total_item.append(item_name)    #item name will enter list of total item
        item_name = item_name.upper()  #item name will be capitalised 
        while True:
            item_code = input("Enter Item Code: ")  #user need to input item code
            if (re.search(pattern_1, item_code)):
                break
            else:
                print("Wrong format. Please try again.")
        item_code = item_code.upper()  #item code will be capitalised
        while True:
            supplier_code = input("Enter Supplier Code: ")  #user need to input supplier code
            if (re.search(pattern_2,supplier_code)):
                break
            else:
                print("Wrong format. Please try again.")
        supplier_code = supplier_code.upper() #supplier code will be capitalised
        while True:
            try:
                stock_quantity = int(input("Enter Quantity in Stock(boxes): ")) #user need to input stock quantity
                if (stock_quantity == 100):
                    break
                else:
                    print("Initial quantity has to be 100.")
            except ValueError: #anything except integer 
                print("Only accept number input!")  #prevent system ValueError terminate the program
        itemlist.append(item_name+","+item_code+","+supplier_code+","+str(stock_quantity))
        newFile = open("ppe.txt","a")   #a new txt file will be open
        newFile.write(item_name+","+item_code+","+supplier_code+","+str(stock_quantity)) #item name, code, supplier code and stock quantity will be recorded in txt file
        newFile.write("\n") #insert a new line after every input
        newFile.close() #close the file after item has been listed
        cont = input("Press <ANY or ENTER> to continue or 'X' to end: ")    #user want whether continue or end the itemlist
        print()
        if ((cont == 'x') or (cont == 'X')):    #itemlist break after 'X' key input
            break
    print("Number of Items: ",len(total_item))  #len mean length of total items
    print("Your inventory list is created...")
    print()
    print('{:<15s} {:<15s} {:<19s} {:<19s}'.format("Item Name", "Item Code", "Supplier Code", "Stock Quantity(boxes)"))    #display table style list of itemlist
    print("---------       ---------       -------------       ---------------------")
    for x in itemlist:
        y = x.split(",")    #split line of the list
        print('{:<15s} {:<15s} {:<19s} {:<19s}'.format(y[0],y[1],y[2],y[3]))    
    #Supplier details
    #Medi-Care Products Sdn Bhd, Taman Ipoh Selatan, 30-A, Lorong Taman Ipoh 1, Ipoh Garden, 31400 Ipoh, Perak, 0555457814, enquiry@medi-care.com.my
    #Fresenius Medical Care Technologies, 8&10, Persiaran Klebang 1, Kawasan Perindustrian 1GB, 31200 Ipoh, Perak, 052915080, enquiry@fresenius.com.my
    #Wellcare Supplier and Services, 17, Laluan Tasek Timur 15, Taman Mewah, Bercham, 31400 Ipoh, Perak, 055451550, enquiry@wellcare.com.my
    print()
    print("Proceeding to create suppliers detail...")
    print("Please enter suppliers' code, company name, address, phone number, and email address accordingly.")  #user need to input supplier code, company name, address, phone number, and email address 
    total_supplier = [] #create empty list for total suppliers after every user input
    while True:
        while True:
            supplier_code = input("Enter Supplier Code: ")  #user need to input supplier code
            if (re.search(pattern_2,supplier_code)):
                break
            else:
                print("Wrong format. Please try again.")
        supplier_code = supplier_code.upper()  #supplier code will be capitalised 
        while True:
            supplier_name = input("Enter Company Name: ")   #user need to input company name
            if (supplier_name == ""):
                print("No blank input!")
            else:
                break
        total_supplier.append(supplier_name)    #company name will enter list of total supplier
        supplier_name = supplier_name.upper()  #supplier name will be capitalised
        while True:
            supplier_address = input("Enter Company Address: ") #user need to input supplier address
            if (supplier_address == ""):
                print("No blank input!")
            else:
                break
        supplier_address = supplier_address.upper()    #supplier address will be capitalised
        while True:
            try:
                supplier_phone = int(input("Enter Company Phone Number Without '-': ")) #user need to input suppliers' phone number
                break
            except ValueError:  #anything except integer
                print("Symbol or Alphabet input is not allowed!")
        while True:
            supplier_email = input("Enter Company Email Address: ") #user need to enter company email address
            if (re.search(pattern_3,supplier_email)):
                break
            else:
                print("Wrong format. Please try again.")
        newSFile = open("suppliers.txt","a")    #a new txt file will open
        newSFile.write(supplier_code+"|"+supplier_name+"|"+supplier_address+"|"+str(supplier_phone)+"|"+supplier_email)  #supplier code,name,address,phone number,email will be recorded in txt file
        newSFile.write("\n")    #insert new line after every input
        newSFile.close()
        print("Supplier detail created...")
        print("Supplier no.",len(total_supplier))   #len mean length value of total suppliers
        print("Following is the detail...")
        print("Supplier Code        : ",supplier_code)
        print("Company Name         : ",supplier_name)
        print("Company Address      : ",supplier_address)
        print("Company Phone Number : ",supplier_phone)
        print("Company Email Address: ",supplier_email)
        cont = input("Press <ANY or ENTER> to continue or 'X' to end: ")    #user want whether continue or end the supplierlist
        print()
        if ((cont == 'x') or (cont == 'X')):
            Main_Menu_Page()
            break

#Menu page for selecting functionalities
def Main_Menu_Page(): 
    print()
    #datetime object containing current date and time
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")   #format of time and date
    print(dt_string)
    print("^^^^^WELCOME ADMIN^^^^^")
    print("-----------------------")
    print("Please select one function: \n1. UPDATE ITEM INVENTORY \n2. TRACK ITEM INVENTORY \n3. SEARCH ITEM INVENTORY \n4. LOG OUT")
    while True:
            option = input("Pick your functionalities <Enter 1 to 4>: ")   #user need to input which functions they wanted
            if (option == "1"):   #user will be lead into Update Item Page if option 1
                Update_Item_Page()
                break
            elif (option == "2"): #user will be lead into Track Item Page if option 2
                Track_Item_Page()
                break
            elif (option == "3"): #user will be lead into Search Item Page if option 3
                Search_Item_Page()
                break
            elif (option == "4"): #user will be lead into Start Up Page if option 4
                print("You have successfully log out!")
                print()
                Start_Up_Page()
                break
            else: #user have to input again if wrong option done
                print("Wrong input!")

#Update Item Inventory Page for Updating Stock Quantities
def Update_Item_Page():
    print()
    print("*****WELCOME TO UPDATE ITEM INVENTORY PAGE*****")
    while True:
        print("Hello admin! Do you wish to increase or decrease item quantities, update supplier details or back to main menu page?")  
        print("[A] Increase Item Quantites [Received from suppliers]")
        print("[B] Decrease Item Quantites [Distributed to hospitals]")
        print("[C] Update Suppliers Details (ONLY 3-4 Suppliers)")
        print("[D] Create or Update Hospitals Details (ONLY 3-4 Hospitals)")
        print("[E] Back to Main Menu Page")
        update = input("Please select one: ")  #user need input one function
        update = update.upper() #a or b or c or d or e input also acceptable
        if (update == "A"): #user will be lead into Increase Item Page if select A
            Increase_Item_Page()
            break
        elif (update == "B"):   #user will be lead into Decrease Item Page if select B
            Decrease_Item_Page()
            break
        elif (update == "C"):   #user will be lead into Update Supplier Page if select C
            Update_Supplier_Page()
            break
        elif (update == "D"):   #user will be lead into Update Hospital Page if select D
            Update_Hospital_Page()
            break
        elif (update == "E"):   #user will be lead into Main Menu Page if select E
            Main_Menu_Page()
            break
        else:
            print("Wrong input! Please enter again!")   #user have to input again if not both A or B

#Increase Item Inventory Page for Increasing Stock Quantities
def Increase_Item_Page():
    print()
    print("*****ADDING RECORD SYSTEM*****")
    print("------------------------------")
    print("Please select and enter your item code, supplier code, and stock quantity wish to add accordingly.")
    print("Item Code: \n1. HC \n2. FS \n3. MS \n4. GL \n5. GW \n6. SC")
    while True:
        add_item_code = input("Pick one item code (Enter 'X' if want to exit): ")   #user need to input the specific item code 
        add_item_code = add_item_code.upper()   #the item code input capitalised
        if ((add_item_code == "HC")or(add_item_code == "FS")or(add_item_code == "MS")or(add_item_code == "GL")or(add_item_code == "GW")or(add_item_code == "SC")):
            newFile = open("ppe.txt","r")   #open file in read mode 
            total_code = [] #empty list for total code for appending
            for L in newFile:
                line = L.split(",") #split elements out from line
                line[3] = int(line[3])  #transform line[3] into integer
                total_code.append(line) #append line into empty list
            for count in total_code:
                if add_item_code in count:
                    num = count[3]  #count[3] represent initial stock quantity
            while True:
                try:
                    add_stock_quantity = int(input("Enter Stock Quantity to Add(boxes): ")) #user need to input stock quantity that wanted to add 
                    print("Input success!")
                    break
                except ValueError:  #anything except integer 
                    print("No other input is allowed!")
            for lists in total_code:
                if add_item_code in lists:
                    lists[3] = lists[3] + add_stock_quantity #lists[3] get updated with sum of initial and added quantity value
                    item_code = lists[1]    #lists[1] represents item code
                else:
                    continue
            newFile.close() #close file after read
            FHand = open("ppe.txt","w") #open file in write mode
            for line in total_code:
                FHand.write(line[0])        #line[0] represents the item name
                FHand.write(",")            #enter "," after line[0] input
                FHand.write(line[1])        #line[1] represents the item code
                FHand.write(",")            #enter "," after line[1] input
                FHand.write(line[2])        #line[2] represents the supplier code
                FHand.write(",")            #enter "," after line[2] input
                FHand.write(str(line[3]))   #line[3] in string form represents stock quantity
                FHand.write("\n")           #enter a new line after line[3] input
            for count in total_code:
                if add_item_code in count:
                    num2 = count[3]     #count[3] represents final stock quantity
            FHand.close()   #close file after write
            print()
            print("Input done!")
            print("Item Code            :", item_code)
            print("Initial Quantity     :", num)
            print("Stock Quantity Added :", add_stock_quantity)
            print("Final Stock Quantity :", num2)
            print('{:<15s} {:<15s} {:<19s} {:<19s}'.format("Item Name", "Item Code", "Supplier Code", "Stock Quantity(boxes)"))    #display table style list of itemlist
            print("---------       ---------       -------------       ---------------------")
            file = open("ppe.txt","r")  #open file in read mode
            for L in file:
                L = L.rstrip()      #remove "\n" out from the lines
                L = L.split(",")    #split elements out from line
                print('{:<15s} {:<15s} {:<19s} {:<19s}'.format(L[0],L[1],L[2],L[3]))
            file.close()
        elif (add_item_code == "X"):    #user will back to Update Item Page if input "x"
            Update_Item_Page()
            break
        else:   #user need to input again if invalid input
            print("Invalid input!")
            continue

#Decrease Item Inventory Page for Decreasing Stock Quantities
def Decrease_Item_Page():
    print()
    print("*****SUBTRACTING RECORD SYSTEM*****")
    print("-----------------------------------")
    print("Below is the current available quantity in stock.")
    print()
    print("-------------------------------------------------------------------------")
    print('{:<15s} {:<15s} {:<19s} {:<19s}'.format("Item Name", "Item Code", "Supplier Code", "Stock Quantity(boxes)"))    #display table style list of itemlist
    print("---------       ---------       -------------       ---------------------")
    file = open("ppe.txt","r")  #open file in read mode
    for L in file:
        L = L.rstrip()  #remove "\n" out from the lines
        L = L.split(",")    #split line of the list
        print('{:<15s} {:<15s} {:<19s} {:<19s}'.format(L[0],L[1],L[2],L[3]))
    file.close()
    print("-------------------------------------------------------------------------")
    print()
    print("Please select the item code that you wish to distribute to hospitals. Hospital details need to be added accordingly.")
    print("Item Code: \n1. HC \n2. FS \n3. MS \n4. GL \n5. GW \n6. SC")
    while True:
        minus_item_code = input("Pick one item code (Enter 'X' if want to exit): ") #user need to input specific item code
        minus_item_code = minus_item_code.upper()
        if ((minus_item_code == "HC")or(minus_item_code == "FS")or(minus_item_code == "MS")or(minus_item_code == "GL")or(minus_item_code == "GW")or(minus_item_code == "SC")):
            newFile = open("ppe.txt","r")   #open file in read mode
            total_code = [] #empty list for total code for appending
            for L in newFile:
                line = L.split(",") #split elements out from line
                line[3] = int(line[3])  #transform line[3] into integer
                total_code.append(line) #append line into empty list of total code
            for count in total_code:
                if minus_item_code in count:
                    num = count[3]  #count[3] represents initial stock quantity
            try:
                distribution_stock_quantity = int(input("Enter Stock Quantity to Distribute(boxes): ")) #user need to input stock quantity to distribute
                if (distribution_stock_quantity < num): #condition when input quantity less than inventory quantity
                    print("Input success! Please input hospital code!")
                    pattern = "[a-zA-Z][a-zA-Z][0-9]"   #pattern for hospital code input
                    while True:
                        hospital_code = input("Enter Hospital Code: ")  #user need to input hospital code
                        hospital_code = hospital_code.upper()   #input for hospital code capitalised
                        if (re.search(pattern,hospital_code)):  #if same pattern match 
                            break
                        else:   #if not same pattern match
                            print("Wrong format. Please try again.")
                    for lists in total_code:
                        if minus_item_code in lists:
                            lists[3] = lists[3] - distribution_stock_quantity #lists[3] get updated with minus of distribution stock quantity
                            item_code = lists[1]    #lists 1 represents item code
                        else:
                            continue
                    newFile.close() #close file after read
                    FHand = open("ppe.txt","w") #open file in write mode
                    for line in total_code:
                        FHand.write(line[0])        #line[0] represents item name
                        FHand.write(",")            #enter a "," after line[0] input 
                        FHand.write(line[1])        #line[1] represents item code
                        FHand.write(",")            #enter a "," after line[1] input
                        FHand.write(line[2])        #line[2] represents supplier code
                        FHand.write(",")            #enter a "," afrer line[2] input
                        FHand.write(str(line[3]))   #line[3] in string form represents stock quantity
                        FHand.write("\n")           #write a new line after every input
                    for count in total_code:    
                        if minus_item_code in count:
                            num2 = count[3]         #count[3] represents final stock quantity
                    FHand.close()
                    print()
                    print("Input done!")
                    print("Item Code                  :", item_code)
                    print("Hospital Code              :", hospital_code)
                    print("Initial Quantity           :", num)
                    print("Stock Quantity Distributed :", distribution_stock_quantity)
                    print("Final Stock Quantity       :", num2)
                    newDFile = open("distribution.txt","a") #a new txt file will open
                    newDFile.write(hospital_code+","+item_code+","+str(distribution_stock_quantity))   #hospital code,item code and stock quantity distributed will be recorded in txt file
                    newDFile.write("\n")    #insert a new line after every input
                    newDFile.close()    #close after open file
                elif (distribution_stock_quantity > num):   #condition when input quantity more than inventory quantity
                    print("Insufficient quantity of stock!")
                    print("Current stock quantity: ", num)
                    print("Please retry with appropriate quantity!")
                    continue
            except ValueError:  #everything except integer
                print("No other input is allowed!")
        elif (minus_item_code == "X"):  #user can exit to Update Item Page using input "X"
            Update_Item_Page()
            break
        else:   #user need to input again if invalid input
            print("Invalid input!")
            continue

#Update Supplier Details Page
    #Supplier details
    #Medi-Care Products Sdn Bhd, Taman Ipoh Selatan, 30-A, Lorong Taman Ipoh 1, Ipoh Garden, 31400 Ipoh, Perak, 0555457814, enquiry@medicare.com.my
    #Fresenius Medical Care Technologies, 8&10, Persiaran Klebang 1, Kawasan Perindustrian 1GB, 31200 Ipoh, Perak, 052915080, enquiry@fresenius.com.my
    #Wellcare Supplier and Services, 17, Laluan Tasek Timur 15, Taman Mewah, Bercham, 31400 Ipoh, Perak, 055451550, enquiry@wellcare.com.my
def Update_Supplier_Page():
    while True:
        print()
        print("Proceeding to update suppliers detail...")
        print("Your current suppliers details format: SupplierCode|SupplierName|SupplierAddress|SupplierPhone|SupplierEmail")
        print()
        pattern = "[a-zA-Z][a-zA-Z][0-9][0-9]"  #pattern for supplier_code input
        pattern_2 = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com.my|edu|net|com|cn)" #pattern for supplier_email input
        suppliers = []  #empty list
        SFile = open("suppliers.txt","r")   #open file in read mode
        for line in SFile:
            line = line.rstrip()    #remove "\n" out from lines
            suppliers.append(line)  #append line into empty list
            print(line)
        SFile.close()   #close file after read
        while True:
            supplier_code = input("Enter Supplier Code to Update: ")    #user need to input supplier code
            supplier_code = supplier_code.upper()   #input supplier code capitalised
            if (re.search(pattern,supplier_code)):  #if pattern for supplier code match
                break
            else:   #if pattern for supplier code not match
                print("Wrong format. Please try again.")
        SFiles = open("suppliers.txt","r")  #open file in read mode
        counter = -1 #set counter for loop
        for lines in SFiles:
            counter += 1 #add 1 for counter for representing number of lines read
            S = lines.split("|")    #split elements out from lines
            if (S[0] == supplier_code): #if elements in file match with input supplier code
                while True:
                    supplier_name = input("Enter Company Name: ")   #user can enter new company name
                    supplier_name = supplier_name.upper()   #input of supplier name capitalised
                    if (supplier_name == ""):   #condition if user enter blank input
                        print("No blank input!")
                    else:
                        break
                while True:
                    supplier_address = input("Enter Company Address: ") #user can enter new company address
                    supplier_address = supplier_address.upper() #input of supplier address capitalised
                    if (supplier_address == ""):    #condition if user enter blank input
                        print("No blank input!")
                    else:
                        break
                while True:
                    try:
                        supplier_phone = int(input("Enter Company Phone Number Without '-': ")) #user need to input company phone number
                        break
                    except ValueError:  #anything except integer
                        print("Symbol or Alphabet input is not allowed!")
                while True:
                    supplier_email = input("Enter Company Email Address: ") #user need to input company email address
                    if (re.search(pattern_2,supplier_email)):   #if pattern for supplier email not match
                        break
                    else:   #if pattern for supplier email not match
                        print("Wrong format. Please try again.")
                suppliers[counter] = supplier_code+"|"+supplier_name+"|"+supplier_address+"|"+str(supplier_phone)+"|"+supplier_email
                WFile = open("suppliers.txt","w")   #open file in write mode
                for Str in suppliers:
                    WFile.write(Str)
                    WFile.write("\n")
                    print(Str)
                break
        WFile.close()
        print()
        print("Update done!")
        cont = input("Press <ANY or ENTER> to continue or 'X' to end: ")    #user want whether continue or end the supplierlist
        print()
        if ((cont == 'x') or (cont == 'X')):
            Main_Menu_Page()
            break

#Update Hospital Details Page
    #Hospital details
    #Penang General Hospital, Jalan Residensi, 10990 George Town, Pulau Pinang, 042225333, hpinang@moh.com.my
    #Pantai Hospital Kuala Lumpur, 8 Jalan Bukit Pantai, 59100 Kuala Lumpur, Malaysia, 0322960888, phkl@pantai.com.my
    #UCSI Hospital, 2, Avenue, 3, Persiaran Springhill, 71010 Port Dickson, Negeri Sembilan, 066488888, info@ucsihospital.com
def Update_Hospital_Page():
    print()
    print("Proceeding to create or update hospital detail...")
    if os.path.isfile("hospitals.txt"):
        Update_Detail()
    else:
        Create_Detail()

#Update Hospital Detail if hospital.txt exist
def Update_Detail():
    while True:
        print()
        print("Proceeding to update hospital detail...")
        print("Your current hospitals details format: HospitalCode|HospitalName|HospitalAddress|HospitalPhone|HospitalEmail")
        print()
        hospital = []   #empty list for appending 
        pattern = "[a-zA-Z][a-zA-Z][0-9]"   #pattern for hospital_code input
        pattern_2 = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com.my|edu|net|com|cn)"   #pattern for hospital_email input
        HFile = open("hospitals.txt","r")   #open file in read mode
        for line in HFile:
            line = line.rstrip()    #remove "\n" for lines in file
            hospital.append(line)   #append line in empty list of hospital
            print(line) #print line in file
        HFile.close()   #close file after read
        while True: 
            hospital_code = input("Enter Hospital Code to Update: ")    #user need to input hospital code
            hospital_code = hospital_code.upper()   #input for hospital code capitalised
            if (re.search(pattern,hospital_code)):  #if pattern match with the input by user
                break
            else:   #if pattern not match with the input by user
                print("Wrong format. Please try again.")
        HFiles = open("hospitals.txt","r")  #open file in read mode
        counter = -1 #set counter to -1
        for lines in HFiles:
            counter += 1 #add counter after read line
            H = lines.split("|")    #split elements out from lines
            if (H[0] == hospital_code): #if line in file match with the input
                while True:
                    hospital_name = input("Enter Hospital Name: ")  #user need to input hospital name
                    hospital_name = hospital_name.upper()   #input of hospital name capitalised
                    if (hospital_name == ""):   #condition if user enter blank input
                        print("No blank input!")
                    else:
                        break
                while True:
                    hospital_address = input("Enter Hospital Address: ")    #user need to input hospital address
                    hospital_address = hospital_address.upper() #input of hospital address capitalised
                    if (hospital_address == ""):    #condition if user enter blank input
                        print("No blank input!")
                    else:
                        break
                while True:
                    try:
                        hospital_phone = int(input("Enter Hospital Phone Number Without '-': "))    #user need to input hospital phone number
                        break
                    except ValueError:  #anything except integer
                        print("Symbol or Alphabet input is not allowed!")
                while True:
                    hospital_email = input("Enter Hospital Email Address: ")    #user need to input hospital email address
                    if (re.search(pattern_2,hospital_email)):   #condition if pattern match with input entered by user
                        break
                    else:   #condition if pattern not match with input entered by user
                        print("Wrong format. Please try again.")
                hospital[counter] = hospital_code+"|"+hospital_name+"|"+hospital_address+"|"+str(hospital_phone)+"|"+hospital_email
                WFile = open("hospitals.txt","w")   #open file in write mode
                for Str in hospital:
                    WFile.write(Str)    #write into file
                    WFile.write("\n")   #write in a new line after every line input
                    print(Str)          #print output after done
                break
        WFile.close()   #close file after write 
        print()
        print("Update done!")
        cont = input("Press <ANY or ENTER> to continue or 'X' to end: ")    #user want whether continue or end the supplierlist
        print()
        if ((cont == 'x') or (cont == 'X')):    #condition if "X" entered
            Main_Menu_Page()
            break

#Create Hospital Detail if hospital.txt does not exist
def Create_Detail():
    print()
    print("Proceeding to create hospitals detail...")
    print("Please enter hospitals' code, hospital name, address, phone number, and email address accordingly.")  #user need to input hospital code, hospital name, address, phone number, and email address
    total_hospital = [] #create empty list for total hospitals after every user input
    pattern = "[a-zA-Z][a-zA-Z][0-9]"   #pattern for hospital_code input
    pattern_2 = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com.my|edu|net|com|cn)"   #pattern for hospital_email input
    while True:
        while True:
            hospital_code = input("Enter Hospital Code: ")  #user need to input hospital code
            hospital_code = hospital_code.upper()  #hospital code will be capitalised 
            if (re.search(pattern,hospital_code)):
                break
            else:
                print("Wrong format. Please try again.")
        while True:
            hospital_name = input("Enter Hospital Name: ")   #user need to input hospital name
            hospital_name = hospital_name.upper()  #hospital name will be capitalised
            if (hospital_name == ""):
                print("No blank input!")
            else:
                break
        total_hospital.append(hospital_name)    #hospital name will enter list of total hospital
        while True:
            hospital_address = input("Enter Hospital Address: ") #user need to input hospital address
            hospital_address = hospital_address.upper()    #hospital address will be capitalised
            if (hospital_address == ""):
                print("No blank input!")
            else:
                break
        while True:
            try:
                hospital_phone = int(input("Enter Hospital Phone Number Without '-': ")) #user need to input hospitals' phone number
                break               
            except ValueError: #anything except integer
                print("Symbol or Alphabet input is not allowed!")
        while True:
            hospital_email = input("Enter Hospital Email Address: ") #user need to enter hospital email address
            if (re.search(pattern_2,hospital_email)):
                break
            else:
                print("Wrong format. Please try again.")
        newHFile = open("hospitals.txt","a")    #a new txt file will open
        newHFile.write(hospital_code+"|"+hospital_name+"|"+hospital_address+"|"+str(hospital_phone)+"|"+hospital_email)  #hospital code,name,address,phone number,email will be recorded in txt file
        newHFile.write("\n")    #insert new line after every input
        newHFile.close()
        print("Hospital detail created...")
        print("Hospital no.",len(total_hospital))   #len mean length value of total hospitals
        print("Following is the detail...")
        print("Hospital Code         : ",hospital_code)
        print("Hospital Name         : ",hospital_name)
        print("Hospital Address      : ",hospital_address)
        print("Hospital Phone Number : ",hospital_phone)
        print("Hospital Email Address: ",hospital_email)
        cont = input("Press <ANY or ENTER> to continue or 'X' to end: ")    #user want whether continue or end the supplierlist
        print()
        if ((cont == 'x') or (cont == 'X')):
            Main_Menu_Page()
            break

#Track Item Inventory Page for printing list
def Track_Item_Page():
    print()
    print("*****TRACKING RECORD SYSTEM*****")
    print("--------------------------------")
    while True:
        print("Please select your option to print:")
        print("  [A]   Total available quantity of all items sorted in ascending order by item code")
        print("  [B]   Records of all items that has stock quantity less than 25 boxes")
        print("[ENTER] Back to Main Menu Page")
        option = input("Enter option: ")    #user need to input which option to proceed
        option = option.upper() #a or b input also acceptable
        if (option == "A"): #enter track function a
            print("#####TOTAL AVAILABLE QUANTITY OF ALL ITEMS SORTED IN ASCENDING ORDER BY ITEM CODE#####")
            print('{:<15s} {:<15s} {:<19s} {:<19s}'.format("Item Name", "Item Code", "Supplier Code", "Stock Quantity(boxes)"))    #display table style list of itemlist
            print("---------       ---------       -------------       ---------------------")
            file = open("ppe.txt","r")  #open file in read mode
            all_item = []   #empty list for appending lines in file
            for L in file:
                L = L.rstrip()  #split elements out from lines
                L = L.split(",")    #split line of the list
                L[3] = int(L[3])    #transform L[3] into integer
                all_item.append(L)  #append line into empty list of all item
            all_item.sort()      #sort all items in ascending order based ALPHABETICALLY
            for line in all_item:
                print('{:<15s} {:<15s} {:<19s} {:<19s}'.format(line[0],line[1],line[2],str(line[3])))
            cont = input("Press <ANY or ENTER> to continue or 'X' to end: ")    #user can either continue or enter 'x' to exit to Main Menu Page
            print()
            if ((cont == 'x') or (cont == 'X')):    #condition if user enter "X"
                Main_Menu_Page()
                break
            file.close()    
        elif (option == "B"):   #enter track function b
            print("#####RECORDS OF ALL ITEMS THAT HAS STOCK QUANTITY LESS THAN 25 BOXES#####")
            print('{:<15s} {:<15s} {:<19s} {:<19s}'.format("Item Name", "Item Code", "Supplier Code", "Stock Quantity(boxes)"))    #display table style list of itemlist
            print("---------       ---------       -------------       ---------------------")
            file = open("ppe.txt","r")
            item_25 = []    #empty list for appending lines in file
            for L in file:
                L = L.rstrip()  #split elements out from lines
                L = L.split(",")    #split line of the list
                L[3] = int(L[3])    #transform L[3] into integer 
                if (int(L[3]) < 25):    #if L[3] less than 25
                    item_25.append(L)   #append line into empty list of item_25
            for line in item_25:
                print('{:<15s} {:<15s} {:<19s} {:<19s}'.format(line[0],line[1],line[2],str(line[3])))
            cont = input("Press <ANY or ENTER> to continue or 'X' to end: ")    #user can either continue or enter 'x' to exit to Main Menu Page
            print()
            if ((cont == 'x') or (cont == 'X')):    #condition if user enter "X"
                Main_Menu_Page()
                break
            file.close()
        elif (option == ""):
            Main_Menu_Page()
            break
        else:   #user need to input again if invalid input
            print("Invalid input! Please try again!")
            
#Search Item Inventory for printing list
def Search_Item_Page():
    while True:
        print()
        myFile = open("distribution.txt","r")   #open file in read mode
        item_code = input("Search Item by respective item code: ")  #user need input item code 
        item_code = item_code.upper()
        if ((item_code == "HC")or(item_code == "FS")or(item_code == "MS")or(item_code == "GL")or(item_code == "GW")or(item_code == "SC")):
            print("Search done!")
            showlist = []   #empty list for storing data in file
            display = []    #empty list for display it into table form after storing data 
            for line in myFile:
                counter = 0 #set counter to 0 representing numebr of lines in file
                L = line.split(",") #split elements out from lines
                if (L[1] == item_code): #condition if line in file match with the item code that entered by user
                    hoscode = L[0]  #set L[0] to hoscode (hospital code)
                    quantity = L[2] #set L[2] to quantity (stock quantity)
                    myFiles = open("distribution.txt","r")  #open file in read mode
                    for lines in myFiles:
                        J = lines.split(",")    #split elements from lines
                        if ((J[0] == hoscode) and (J[1] == item_code)): #condition if lines in file match with hoscode and item code
                            counter += 1 #add 1 counter accordingly
                            if (counter > 1):   #condition if counter more than 1
                                quantity = int(quantity) + int(J[2])    #quantity represents the sum of quantity
                    x = 1 #set x to 1 
                    for Str in showlist:
                        K = Str.split(",")  #split elements out from lines
                        if (K[0] == hoscode):   #if line in file match with hoscode
                            x = 0 #set x to 0 
                            break
                    if (x == 1):    #condition if x is at 1
                        showlist.append(hoscode+","+item_code+","+str(quantity))    #append into empty list of showlist
            print("ITEM CODE: ",item_code)
            print('{:<15s} {:<15s} {:<20s}'.format("Hospital Code", "Item Code", "Stock Quantity(boxes)"))    #display table style list of itemlist
            print("-------------   ---------       ---------------------")
            for items in showlist:
                items = items.rstrip()  #remove "\n" from lines
                items = items.split(",")    #split elements out from lines
                display.append(items)   #append into empty list of display
            for line in display:
                print('{:<15s} {:<15s} {:<20s}'.format(line[0], line[1], str(line[2])))
            myFile.close()  #close file after read
            cont = input("Press <ANY or ENTER> to continue or 'X' to end: ")    #user can exit to Main Menu Page if enter "X"
            print()
            if ((cont == 'x') or (cont == 'X')):    #condition if "X" is entered by user
                Main_Menu_Page()
                break
        else:
            print("Invalid item code! Please try again!")

#REAL PROGRAM LAUNCH
Start_Up_Page()
