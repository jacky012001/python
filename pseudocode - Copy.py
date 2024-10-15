#JACKY WONG CHUN KIT
#TP066984

#Main Homepage of PPE System
FUNCTION Start_Up_Page()
BEGIN
    DECLARE username,password
    Print"This program is created by:"
    Print"Student Name : JACKY WONG CHUN KIT"
    Print"TP Number    : TP066984"
    Print""
    DOWHILE (condition == TRUE)
        Print"*****WELCOME TO INVENTORY MANAGEMENT SYSTEM FOR PERSONAL PROTECTIVE EQUIPMENT(PPE)*****"
        Print"---------------------------------------------------------------------------------------"
        Print"Please login your account!"
        Print"Username:"
        Read username
        Print"Password:"
        Read password
        IF ((username == "admin")AND(password == "abc123"))THEN
            Print"LOGIN SUCCESS!"
            call First_Creation_Confirm_Page()
            BREAK
        ELSE
            IF ((username == "")AND(password == ""))THEN
                Print"Thank you for using this program! See you!"
                BREAK
            ELSE
                Print"INVALID Username or Password! Please login again!"
                Print""
                Prompt user
            ENDIF
        ENDIF
    ENDDO
END
    
#Initial Inventory Confirmation Page
FUNCTION First_Creation_Confirm_Page()
BEGIN
    DECLARE option
    Print""
    Print"*****WELCOME ADMIN! IS THIS THE FIRST TIME PROGRAM EXECUTED?*****"
    Print"-----------------------------------------------------------------"
    Print"    [A]  Yes\n    [B]  No\n   [ANY] Exit"
    Print""
    Read option
    option := upper(option)
    IF (option == "A")THEN
        IF (path_is_valid, "ppe.txt")THEN
            Print"File already exist! Please proceed to Menu Page!"
            call First_Creation_Confirm_Page()
        ELSE
            call First_Creation_Page()
        ENDIF
    ELSE
        IF (option == "B")THEN
            IF (path_is_valid,"ppe.txt")THEN
                call Main_Menu_Page()
            ELSE
                Print"No existing data! Please create initial inventory!"
                call First_Creation_Confirm_Page()
            ENDIF
        ELSE
            Print"Proceeding to Start Up Page..."
            Print""
            call Start_Up_Page()
        ENDIF
    ENDIF
END
    
#Initial Inventory Creation Page
FUNCTION First_Creation_Page()
BEGIN
    DECLARE item_name,item_code,supplier_code,stock_quantity
    DECLARE supplier_code,supplier_name,supplier_address,supplier_phone,supplier_email,cont,choice
    Print""
    Print"Creating Initial Inventory..."
    Print"Please enter your item name, item code, supplier code and stock quantity accordingly."
    ASSIGN EMPTY LIST TO itemlist
    ASSIGN EMPTY LIST TO total_item
    ASSIGN [a-zA-Z] TO pattern_1
    ASSIGN [a-zA-Z][a-zA-Z][0-9][0-9] TO pattern_2
    ASSIGN [a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net) TO pattern_3
    DOWHILE (condition == TRUE)
        DOWHILE (condition == TRUE)
            Print"Enter Item Name: "
            Read item_name
            IF (re.search(pattern_1, item_name))THEN
                BREAK
            ELSE
                Print"Wrong format. Please try again."
                Prompt user
            ENDIF
        ENDDO
        APPEND item_name TO total_item
        item_name := upper(item_name)
        DOWHILE (condition == TRUE)
            Print"Enter Item Code: "
            Read item_code
            IF (re.search(pattern_1, item_code))THEN
                BREAK
            ELSE
                Print"Wrong format. Please try again."
                Prompt user
            ENDIF
        ENDDO
        item_code := upper(item_code)
        DOWHILE (condition == TRUE)
            Print"Enter Supplier Code: "
            Read supplier_code
            IF (re.search(pattern_2, supplier_code))THEN
                BREAK
            ELSE
                Print"Wrong format. Please try again."
                Prompt user
            ENDIF
        ENDDO
        supplier_code := upper(supplier_code)
        DOWHILE (condition == TRUE)
            TRY stock_quantity
                Print"Enter Quantity in Stock(boxes): "
                Read stock_quantity
                IF (stock_quantity == 100)THEN
                    BREAK
                ELSE
                    Print"Initial quantity has to be 100."
                    Prompt user
                ENDIF
            EXCEPT ValueError
                Print"Only accept number input!"
                Prompt user
        ENDDO
        APPEND item_name+","+item_code+","+supplier_code+","+STRING(stock_quantity) TO itemlist
        OPENFILE "ppe.txt" FOR APPEND AS newFile
        WRITEFILE "ppe.txt", "item_name+","+item_code+","+supplier_code+","+str(stock_quantity)"
        WRITEFILE "ppe.txt", "\n"
        CLOSEFILE "ppe.txt"
        Print"Press <ANY or ENTER> to continue or 'X' to end: "
        Read cont
        Print""
        IF ((cont == 'x')OR(cont == 'X'))THEN
            BREAK
        ENDIF
    ENDDO
    Print'"Number of Items: ",len(total_item)'
    Print"Your inventory list is created..."
    Print""
    Print"'{:<15s} {:<15s} {:19s} {:<19s}'.format('Item Name', 'Item Code', 'Supplier Code', 'Stock Quantity(boxes)')"
    Print"---------       ---------       -------------       ---------------------"
    LOOP x IN itemlist
        ASSIGN y TO SPLIT(x, ",")
        Print"'{:<15s} {:<15s} {:<19s} {:<19s}'.format(y[0],y[1],y[2],y[3])"
        NEXT x
    ENDLOOP
    Print""
    Print"Proceeding to create suppliers detail..."
    Print"Please enter suppliers' code, company name, address, phone number, and email address accordingly."
    ASSIGN EMPTY LIST TO total_supplier
    DOWHILE (condition == TRUE)
        DOWHILE (condition == TRUE)
            Print"Enter Supplier Code: "
            Read supplier_code
            IF (re.search(pattern_2, supplier_code))THEN
                BREAK
            ELSE
                Print"Wrong format. Please try again."
                Prompt user
            ENDIF
        ENDDO
        supplier_code := upper(supplier_code)
        DOWHILE (condition == TRUE)
            Print"Enter Company Name: "
            Read supplier_name
            IF (supplier_name == "")THEN
                Print"No blank input!"
                Prompt user
            ELSE
                BREAK
            ENDIF
        ENDDO
        APPEND supplier_name TO total_supplier
        supplier_name := upper(supplier_name)
        DOWHILE (condition == TRUE)
            Print"Enter Company Address: "
            Read supplier_address
            IF (supplier_address == "")THEN
                Print"No blank input!"
                Prompt user
            ELSE
                BREAK
            ENDIF
        ENDDO
        supplier_address := upper(supplier_address)
        DOWHILE (condition == TRUE)
            TRY supplier_phone
                Print"Enter Company Phone Number Without '-': "
                Read supplier_phone
                BREAK
            EXCEPT ValueError
                Print"Symbol or Alphabet input is not allowed!"
                Prompt user
        ENDDO
        DOWHILE (condition == TRUE)
            Print"Enter Company Email Address: "
            Read supplier_email
            IF (re.search(pattern_3,supplier_email))THEN
                BREAK
            ELSE
                Print"Wrong format. Please try again."
                Prompt user
            ENDIF
        ENDDO
        OPENFILE "suppliers.txt" FOR APPEND AS newSFile
        WRITEFILE "suppliers.txt","supplier_code+"|"+supplier_name+"|"+supplier_address+"|"+str(supplier_phone)+"|"+supplier_email"
        WRITEFILE "suppliers.txt","\n"
        CLOSEFILE "suppliers.txt"
        Print"Supplier detail created..."
        Print"Supplier no.",len(total_supplier)
        Print"Following is the detail..."
        Print"Supplier Code        : ",supplier_code
        Print"Company Name         : ",supplier_name
        Print"Company Address      : ",supplier_address
        Print"Company Phone Number : ",supplier_phone
        Print"Company Email Address: ",supplier_email
        Print"Press <ANY or ENTER> to continue or 'X' to end: "
        Read cont
        Print""
        IF ((cont == 'x')OR(cont == 'X'))THEN
            call Main_Menu_Page()
            BREAK
        ENDIF
    ENDDO
END

#Menu Page for selecting functionalities
FUNCTION Main_Menu_Page()
BEGIN
    DECLARE option
    Print""
    ASSIGN datetime.now() TO now
    ASSIGN now.strftime("%d/%m/%Y %H:%M:%S") TO dt_string
    Print dt_string
    Print"^^^^^WELCOME ADMIN^^^^^"
    Print"-----------------------"
    Print"Please select one function: \n1. UPDATE ITEM INVENTORY \n2. TRACK ITEM INVENTORY \n3. SEARCH ITEM INVENTORY \n4. LOG OUT"
    DOWHILE (condition == TRUE)
        Print"Pick your functionalities <Enter 1 to 4>: "
        Read option
        IF (option == "1")THEN
            call Update_Item_Page()
            BREAK
        ELSE
            IF (option == "2")THEN
                call Track_Item_Page()
                BREAK
            ELSE
                IF (option == "3")THEN
                    call Search_Item_Page()
                    BREAK
                ELSE
                    IF (option == "4")THEN
                        Print"You have successfully log out!"
                        Print""
                        call Start_Up_Page()
                        BREAK
                    ELSE
                        Print"Wrong input!"
                        Prompt user
                    ENDIF
                ENDIF
            ENDIF
        ENDIF
    ENDDO
END
            
#Update Item Inventory Page for Updating Stock Quantites
FUNCTION Update_Item_Page()
BEGIN
    DECLARE update
    Print""
    Print"*****WELCOME TO UPDATE ITEM INVENTORY PAGE*****"
    DOWHILE (condition == TRUE)
        Print"Hello admin! Do you wish to increase or decrease item quantities, update supplier details or back to main menu page?"
        Print"[A] Increase Item Quantites [Received from suppliers]"
        Print"[B] Decrease Item Quantites [Distributed to hospitals]"
        Print"[C] Update Suppliers Details (ONLY 3-4 Suppliers)"
        Print"[D] Create or Update Hospitals Details (ONLY 3-4 Hospitals)"
        Print"[E] Back to Main Menu Page"
        Print"Please select one: "
        Read update
        update := upper(update)
        IF (update == "A")THEN
            call Increase_Item_Page()
            BREAK
        ELSE
            IF (update == "B")THEN
                call Decrease_Item_Page()
                BREAK
            ELSE
                IF (update == "C")THEN
                    call Update_Supplier_Page()
                    BREAK
                ELSE
                    IF (update == "D")THEN
                        call Update_Hospital_Page()
                        BREAK
                    ELSE
                        IF (update == "E")THEN
                            call Main_Menu_Page()
                            BREAK
                        ELSE
                            Print"Wrong input! Please enter again!"
                            Prompt user
                        ENDIF
                    ENDIF
                ENDIF
            ENDIF
        ENDIF
    ENDDO
END

#Increase Item Inventory Page for Increasing Stock Quantites
FUNCTION Increase_Item_Page()
BEGIN
    DECLARE add_item_code,add_stock_quantity
    Print""
    Print"*****ADDING RECORD SYSTEM*****"
    Print"------------------------------"
    Print"Please select and enter your item code, supplier code, and stock quantity wish to add accordingly."
    Print"Item Code: \n1. HC \n2. FS \n3. MS \n4. GL \n5. GW \n6. SC"
    DOWHILE (condition == TRUE)
        Print"Pick one item code (Enter 'X' if want to exit): "
        Read add_item_code
        add_item_code := upper(add_item_code)
        IF ((add_item_code == "HC")OR(add_item_code == "FS")OR(add_item_code == "MS")OR(add_item_code == "GL")OR(add_item_code == "GW")OR(add_item_code == "SC"))THEN
            OPENFILE "ppe.txt" FOR READ AS newFile
            ASSIGN EMPTY LIST TO total_code
            LOOP L IN newFile
                ASSIGN SPLIT(L, ",") TO line
                DECLARE line[3] : INTEGER
                APPEND line TO total_code
                NEXT L
            ENDLOOP
            LOOP count IN total_code
                IF add_item_code IN count THEN
                    ASSIGN count[3] TO num
                ENDIF
                NEXT count
            ENDLOOP
            DOWHILE (condition == TRUE)
                TRY add_stock_quantity
                    Print"Enter Stock Quantity to Add(boxes): "
                    Read add_stock_quantity
                    Print"Input success!"
                    BREAK
                EXCEPT ValueError
                    Print"No other input is allowed!"
                    Prompt user
            LOOP lists IN total_code
                IF add_item_code IN lists THEN
                    lists[3] = lists[3] + add_stock_quantity
                    ASSIGN lists[1] TO item_code
                ELSE
                    CONTINUE
                ENDIF
                NEXT lists
            ENDLOOP
            CLOSEFILE "ppe.txt"
            OPENFILE "ppe.txt" FOR WRITE AS FHand
            LOOP line IN total_code
                WRITEFILE "ppe.txt","line[0]"
                WRITEFILE "ppe.txt",","
                WRITEFILE "ppe.txt","line[1]"
                WRITEFILE "ppe.txt",","
                WRITEFILE "ppe.txt","line[2]"
                WRITEFILE "ppe.txt",","
                WRITEFILE "ppe.txt","str(line[3])"
                WRITEFILE "ppe.txt","\n"
                NEXT line
            ENDLOOP
            LOOP count IN total_code
                IF add_item_code IN count THEN
                    ASSIGN count[3] TO num2
                ENDIF
                NEXT count
            ENDLOOP
            CLOSEFILE "ppe.txt"
            Print""
            Print"Input done!"
            Print"Item Code            :", item_code
            Print"Initial Quantity     :", num
            Print"Stock Quantity Added :", add_stock_quantity
            Print"Final Stock Quantity :", num2
            Print'{:<15s} {:<15s} {:<19s} {:<19s}'.format("Item Name", "Item Code", "Supplier Code", "Stock Quantity(boxes)")
            Print"---------       ---------       -------------       ---------------------"
            OPENFILE "ppe.txt" FOR READ AS file
            LOOP L IN file
                ASSIGN RSTRIP(L,"") TO L
                ASSIGN SPLIT(L,",") TO L
                Print'{:<15s} {:<15s} {:<19s} {:<19s}'.format(L[0],L[1],L[2],L[3])
                NEXT L
            ENDLOOP
            CLOSEFILE "ppe.txt"
        ELSE
            IF (add_item_code == "X")THEN
                call Update_Item_Page()
                BREAK
            ELSE
                Print"Invalid input!"
                Prompt user
                CONTINUE
            ENDIF
        ENDIF
    ENDDO
END

#Decrease Item Inventory Page for Decreasing Stock Quantites
FUNCTION Decrease_Item_Page()
BEGIN
    DECLARE minus_item_code,distribution_stock_quantity,hospital_code
    Print""
    Print"*****SUBTRACTING RECORD SYSTEM*****"
    Print"-----------------------------------"
    Print"Below is the current available quantity in stock."
    Print""
    Print"-------------------------------------------------------------------------"
    Print'{:<15s} {:<15s} {:<19s} {:<19s}'.format("Item Name", "Item Code", "Supplier Code", "Stock Quantity(boxes)")
    Print"---------       ---------       -------------       ---------------------"
    OPENFILE "ppe.txt" FOR READ AS file
    LOOP L IN file
        ASSIGN RSTRIP(L,"") TO L
        ASSIGN SPLIT(L,",") TO L
        Print'{:<15s} {:<15s} {:<19s} {:<19s}'.format(L[0],L[1],L[2],L[3])
        NEXT L
    ENDLOOP
    CLOSEFILE "ppe.txt"
    Print"-------------------------------------------------------------------------"
    Print""
    Print"Please select the item code that you wish to distribute to hospitals. Hospital details need to be added accordingly."
    Print"Item Code: \n1. HC \n2. FS \n3. MS \n4. GL \n5. GW \n6. SC"
    DOWHILE (condition == TRUE)
        Print"Pick one item code (Enter 'X' if want to exit): "
        Read minus_item_code
        minus_item_code := upper(minus_item_code)
        IF ((minus_item_code == "HC")OR(minus_item_code == "FS")OR(minus_item_code == "MS")OR(minus_item_code == "GL")OR(minus_item_code == "GW")OR(minus_item_code == "SC"))THEN
            OPENFILE "ppe.txt" FOR READ AS newFile
            ASSIGN EMPTY LIST TO total_code
            LOOP L IN newFile
                ASSIGN SPLIT(L,",") TO line
                DECLARE line[3] : INTEGER
                APPEND line TO total_code
                NEXT L
            ENDLOOP
            LOOP count IN total_code
                IF minus_item_code IN count THEN
                    ASSIGN count[3] TO num
                ENDIF
                NEXT count
            ENDLOOP
            TRY distribution_stock_quantity
                Print"Enter Stock Quantity to Distribute(boxes): "
                Read distribution_stock_quantity
                IF (distribution_stock_quantity < num)THEN
                    Print"Input success! Please input hospital code!"
                    ASSIGN [a-zA-Z][a-zA-Z][0-9] TO pattern
                    DOWHILE (condition == TRUE)
                        Print"Enter Hospital Code: "
                        Read hospital_code
                        hospital_code := upper(hospital_code)
                        IF (re.search(pattern,hospital_code))THEN
                            BREAK
                        ELSE
                            Print"Wrong format. Please try again."
                        ENDIF
                    ENDDO
                    LOOP lists IN total_code
                        IF minus_item_code IN lists THEN
                            lists[3] = lists[3] - distribution_stock_quantity
                            ASSIGN lists[1] TO item_code
                        ELSE
                            CONTINUE
                        ENDIF
                        NEXT lists
                    ENDLOOP
                    CLOSEFILE "ppe.txt"
                    OPENFILE "ppe.txt" FOR WRITE AS FHand
                    LOOP line IN total_code
                        WRITEFILE "ppe.txt","line[0]"
                        WRITEFILE "ppe.txt",","
                        WRITEFILE "ppe.txt","line[1]"
                        WRITEFILE "ppe.txt",","
                        WRITEFILE "ppe.txt","line[2]"
                        WRITEFILE "ppe.txt",","
                        WRITEFILE "ppe.txt","str(line[3])"
                        WRITEFILE "ppe.txt","\n"
                        NEXT line
                    ENDLOOP
                    LOOP count IN total_code
                        IF minus_item_code IN count THEN
                            ASSIGN count[3] TO num2
                        ENDIF
                        NEXT count
                    ENDLOOP
                    CLOSEFILE "ppe.txt"
                    Print""
                    Print"Input done!"
                    Print"Item Code                  :", item_code
                    Print"Hospital Code              :", hospital_code
                    Print"Initial Quantity           :", num
                    Print"Stock Quantity Distributed :", distribution_stock_quantity
                    Print"Final Stock Quantity       :", num2
                    OPENFILE "distribution.txt" FOR APPEND AS newDFile
                    WRITEFILE "distribution.txt",'hospital_code+","+item_code+","+str(distribution_stock_quantity)'
                    WRITEFILE "distribution.txt","\n"
                    CLOSEFILE "distribution.txt"
                ELSE
                    IF (distribution_stock_quantity > num)THEN
                        Print"Insufficient quantity of stock!"
                        Print"Current stock quantity: ", num
                        Print"Please retry with appropriate quantity!"
                        Prompt user
                        CONTINUE
                    ENDIF
                ENDIF
            EXCEPT ValueError
                Print"No other input is allowed!"
                Prompt user
        ELSE
            IF (minus_item_code == "X")THEN
                call Update_Item_Page()
                BREAK
            ELSE
                Print"Invalid input!"
                Prompt user
                CONTINUE
            ENDIF
        ENDIF
    ENDDO
END

#Update Supplier Detail Page
FUNCTION Update_Supplier_Page()
BEGIN
    DECLARE supplier_code,supplier_name,supplier_address,supplier_phone,supplier_email,cont
   DOWHILE (condition == TRUE)
        Print""
        Print"Proceeding to update suppliers detail..."
        Print"Your current suppliers details format: SupplierCode|SupplierName|SupplierAddress|SupplierPhone|SupplierEmail"
        Print""
        ASSIGN [a-zA-Z][a-zA-Z][0-9][0-9] TO pattern
        ASSIGN [a-zA-Z0-9]+@[a-zA-Z]+\.(com.my|edu|net|com|cn) TO pattern_2
        ASSIGN EMPTY LIST TO suppliers
        OPENFILE "suppliers.txt" FOR READ AS SFile
        LOOP line IN SFile
            ASSIGN RSTRIP(line,"") TO line
            APPEND line TO suppliers
            Print line
            NEXT line
        ENDLOOP
        CLOSEFILE "suppliers.txt"
        DOWHILE (condition == TRUE)
            Print"Enter Supplier Code to Update: "
            Read supplier_code
            supplier_code := upper(supplier_code)
            IF (re.search(pattern,supplier_code))THEN
                BREAK
            ELSE
                Print"Wrong format. Please try again."
                Prompt user
            ENDIF
        ENDDO
        OPENFILE "suppliers.txt" FOR READ AS SFiles
        counter := -1
        LOOP lines IN SFiles
            counter := counter + 1
            ASSIGN SPLIT(lines,"|") TO S
            IF (S[0] == supplier_code)THEN
                DOWHILE (condition == TRUE)
                    Print"Enter Company Name: "
                    Read supplier_name
                    supplier_name := upper(supplier_name)
                    IF (supplier_name == "")THEN
                        Print"No blank input!"
                        Prompt user
                    ELSE
                        BREAK
                    ENDIF
                ENDDO
                DOWHILE (condition == TRUE)
                    Print"Enter Company Address: "
                    supplier_address := upper(supplier_address)
                    IF (supplier_address == "")THEN
                        Print"No blank input!"
                        Prompt user
                    ELSE
                        BREAK
                    ENDIF
                ENDDO
                DOWHILE (condition == TRUE)
                    TRY supplier_phone
                        Print"Enter Company Phone Number Without '-': "
                        Read supplier_phone
                        BREAK
                    EXCEPT ValueError
                        Print"Symbol or Alphabet input is not allowed!"
                        Prompt user
                ENDDO
                DOWHILE (condition == TRUE)
                    Print"Enter Company Email Address: "
                    Read supplier_email
                    IF (re.search(pattern_2,supplier_email))THEN
                        BREAK
                    ELSE
                        Print"Wrong format. Please try again."
                        Prompt user
                    ENDIF
                ENDDO
                ASSIGN supplier_code+"|"+supplier_name+"|"+supplier_address+"|"+str(supplier_phone)+"|"+supplier_email TO suppliers[counter]
                OPENFILE "suppliers.txt" FOR WRITE AS WFile
                LOOP Str IN suppliers
                    WRITEFILE "suppliers.txt",Str
                    WRITEFILE "suppliers.txt","\n"
                    Print Str
                    NEXT Str
                ENDLOOP
                ENDDO
            ENDIF
            NEXT lines
        ENDLOOP
        CLOSEFILE "suppliers.txt"
        Print""
        Print"Update done!"
        Print"Press <ANY or ENTER> to continue or 'X' to end: "
        Read cont
        Print""
        IF ((cont == 'x')OR(cont == 'X'))THEN
            call Main_Menu_Page()
            BREAK
        ELSE
            CONTINUE
        ENDIF
    ENDDO
END

#Update Hospital Details Page
FUNCTION Update_Hospital_Page()
BEGIN
    Print""
    Print"Proceeding to create or update hospital detail..."
    IF (path_is_valid, "ppe.txt")THEN
        call Update_Detail()
    ELSE
        call Create_Detail()
    ENDIF
END

#Update Hospital Detail if hospital.txt exist
FUNCTION Update_Detail()
BEGIN
    DECLARE hospital_code,hospital_name,hospital_address,hospital_phone,hospital_email,cont
    DOWHILE (condition == TRUE)
        Print""
        Print"Proceeding to update hospital detail..."
        Print"Your current hospitals details format: HospitalCode|HospitalName|HospitalAddress|HospitalPhone|HospitalEmail"
        Print""
        ASSIGN EMPTY LIST TO hospital
        ASSIGN [a-zA-Z][a-zA-Z][0-9] TO pattern
        ASSIGN [a-zA-Z0-9]+@[a-zA-Z]+\.(com.my|edu|net|com|cn) TO pattern_2
        OPENFILE "hospitals.txt" FOR READ AS HFile
        LOOP line IN HFile
            ASSIGN RSTRIP(line,"") TO line
            APPEND line TO hospital
            Print line
            NEXT line
        ENDLOOP
        CLOSEFILE "hospitals.txt"
        DOWHILE (condition == TRUE)
            Print"Enter Hospital Code to Update: "
            Read hospital_code
            hospital_code := upper(hospital_code)
            IF (re.search(pattern,hospital_code))THEN
                BREAK
            ELSE
                Print"Wrong format. Please try again."
                Prompt user
            ENDIF
        ENDDO
        OPENFILE "hospitals.txt" FOR READ AS HFiles
        counter := -1
        LOOP lines IN HFiles
            counter := counter + 1
            ASSIGN SPLIT(lines,"|") TO H
            IF (H[0] == hospital_code)THEN
                DOWHILE (condition == TRUE)
                    Print"Enter Hospital Name: "
                    Read hospital_name
                    hospital_name := upper(hospital_name)
                    IF (hospital_name == "")THEN
                        Print"No blank input!"
                        Prompt user
                    ELSE
                        BREAK
                    ENDIF
                ENDDO
                DOWHILE (condition == TRUE)
                    Print"Enter Hospital Address: "
                    Read hospital_address
                    hospital_address := upper(hospital_address)
                    IF (hospital_address == "")THEN
                        Print"No blank input!"
                        Prompt user
                    ELSE
                        BREAK
                    ENDIF
                ENDDO
                DOWHILE (condition == TRUE)
                    TRY hospital_phone
                        Print"Enter Hospital Phone Number Without '-': "
                        Read hospital_phone
                        BREAK
                    EXCEPT ValueError
                        Print"Symbol or Alphabet input is not allowed!"
                        Prompt user
                ENDDO
                DOWHILE (condition == TRUE)
                    Print"Enter Hospital Email Address: "
                    Read hospital_email
                    IF (re.search(pattern_2,hospital_email))THEN
                        BREAK
                    ELSE
                        Print"Wrong format. Please try again."
                        Prompt user
                    ENDIF
                ENDDO
                ASSIGN hospital_code+"|"+hospital_name+"|"+hospital_address+"|"+str(hospital_phone)+"|"+hospital_email TO hospital[counter]
                OPENFILE "hospitals.txt" FOR WRITE AS WFile
                LOOP Str IN hospital
                    WRITEFILE "hospitals.txt", Str
                    WRITEFILE "hospitals.txt", "\n"
                    Print Str
                    NEXT Str
                ENDLOOP
                ENDDO
            ENDIF
            NEXT lines
        ENDLOOP
        CLOSEFILE "hospitals.txt"
        Print""
        Print"Update done!"
        Print"Press <ANY or ENTER> to continue or 'X' to end: "
        Read cont
        Print""
        IF ((cont == 'x')OR(cont == 'X'))THEN
            call Main_Menu_Page()
            BREAK
        ELSE
            CONTINUE
        ENDIF
    ENDDO
END

#Create Hospital Detail if hospital.txt does not exist
FUNCTION Create_Detail()
BEGIN
    DECLARE hospital_code,hospital_name,hospital_address,hospital_phone,hospital_email,cont
    Print""
    Print"Proceeding to create hospitals detail..."
    Print"Please enter hospitals' code, hospital name, address, phone number, and email address accordingly."
    ASSIGN EMPTY LIST TO total_hospital
    ASSIGN [a-zA-Z][a-zA-Z][0-9] TO pattern
    ASSIGN [a-zA-Z0-9]+@[a-zA-Z]+\.(com.my|edu|net|com|cn) TO pattern_2
    DOWHILE (condition == TRUE)
        DOWHILE (condition == TRUE)
            Print"Enter Hospital Code: "
            Read hospital_code
            hospital_code := upper(hospital_code)
            IF (re.search(pattern,hospital_code))THEN
                BREAK
            ELSE
                Print"Wrong format. Please try again."
                Prompt user
            ENDIF
        ENDDO
        DOWHILE (condition == TRUE)
            Print"Enter Hospital Name: "
            Read hospital_name
            hospital_name := upper(hospital_name)
            IF (hospital_name == "")THEN
                Print"No blank input!"
                Prompt user
            ELSE
                BREAK
            ENDIF
        ENDDO
        APPEND hospital_name TO total_hospital
        DOWHILE (condition == TRUE)
            Print"Enter Hospital Address: "
            Read hospital_address
            hospital_address := upper(hospital_address)
            IF (hospital_address == "")THEN
                Print"No blank input!"
                Prompt user
            ELSE
                BREAK
            ENDIF
        ENDDO
        DOWHILE (condition == TRUE)
            TRY hospital_phone
                Print"Enter Hospital Phone Number Without '-': "
                Read hospital_phone
                BREAK
            EXCEPT ValueError
                Print"Symbol or Alphabet input is not allowed!"
                Prompt user
        ENDDO
        DOWHILE (condition == TRUE)
            Print "Enter Hospital Email Address: "
            Read hospital_email
            IF (re.search(pattern_2,hospital_email))THEN
                BREAK
            ELSE
                Print"Wrong format. Please try again."
                Prompt user
            ENDIF
        ENDDO
        OPENFILE "hospitals.txt" FOR APPEND AS newHFile
        WRITEFILE "hospitals.txt", hospital_code+"|"+hospital_name+"|"+hospital_address+"|"+str(hospital_phone)+"|"+hospital_email
        WRITEFILE "hospitals.txt", "\n"
        CLOSEFILE "hospitals.txt"
        Print"Hospital detail created..."
        Print"Hospital no.",len(total_hospital)
        Print"Following is the detail..."
        Print"Hospital Code         : ",hospital_code
        Print"Hospital Name         : ",hospital_name
        Print"Hospital Address      : ",hospital_address
        Print"Hospital Phone Number : ",hospital_phone
        Print"Hospital Email Address: ",hospital_email
        Print"Press <ANY or ENTER> to continue or 'X' to end: "
        Read cont
        Print""
        IF ((cont == 'x')OR(cont == 'X'))THEN
            call Main_Menu_Page()
            BREAK
        ENDIF
    ENDDO
END

#Track Item Inventory Page for Printing list
FUNCTION Track_item_Page()
BEGIN
    DECLARE option,cont
    Print""
    Print"*****TRACKING RECORD SYSTEM*****"
    Print"--------------------------------"
    DOWHILE (condition == TRUE)
        Print"Please select your option to print:"
        Print"  [A]   Total available quantity of all items sorted in ascending order by item code"
        Print"  [B]   Records of all items that has stock quantity less than 25 boxes"
        Print"[ENTER] Back to Main Menu Page"
        Print"Enter option: "
        Read option
        option := upper(option)
        IF (option == "A")THEN
            Print"#####TOTAL AVAILABLE QUANTITY OF ALL ITEMS SORTED IN ASCENDING ORDER BY ITEM CODE#####"
            Print"'{:<15s} {:<15s} {:<19s} {:<19s}'.format('Item Name', 'Item Code', 'Supplier Code', 'Stock Quantity(boxes)'"
            Print"---------       ---------       -------------       ---------------------"
            OPENFILE "ppe.txt" FOR READ AS file
            ASSIGN EMPTY LIST TO all_item
            LOOP L IN file
                ASSIGN RSTRIP(L,"") TO L
                ASSIGN SPLIT(L,",") TO L
                DECLARE L[3] : INTEGER
                APPEND L TO all_item
                NEXT L
            ENDLOOP
            SORT all_item
            LOOP line IN all_item
                Print'{:<15s} {:<15s} {:<19s} {:<19s}'.format(line[0],line[1],line[2],str(line[3]))
                NEXT line
            ENDLOOP
            Print"Press <ANY or ENTER> to continue or 'X' to end: "
            Read cont
            Print""
            IF ((cont == 'x') or (cont == 'X'))THEN
                call Main_Menu_Page()
                BREAK
            ENDIF
            CLOSEFILE "ppe.txt"
        ELSE
            IF (option == "B")THEN
                Print"#####RECORDS OF ALL ITEMS THAT HAS STOCK QUANTITY LESS THAN 25 BOXES#####"
                Print"'{:<15s} {:<15s} {:<19s} {:<19s}'.format('Item Name', 'Item Code', 'Supplier Code', 'Stock Quantity(boxes)'"
                Print"---------       ---------       -------------       ---------------------"
                OPENFILE "ppe.txt" FOR READ AS file
                ASSIGN EMPTY LIST TO item_25
                LOOP L IN file
                    ASSIGN RSTRIP(L,"") TO L
                    ASSIGN SPLIT(L,",") TO L
                    DECLARE L[3] : INTEGER
                    IF (L[3] < 25)THEN
                        APPEND L TO item_25
                    ENDIF
                    NEXT L
                ENDLOOP
                LOOP line IN item_25
                    Print'{:<15s} {:<15s} {:<19s} {:<19s}'.format(line[0],line[1],line[2],str(line[3]))
                    NEXT line
                ENDLOOP
                Print"Press <ANY or ENTER> to continue or 'X' to end: "
                Read cont
                Print""
                IF ((cont == 'x')OR(cont == 'X'))THEN
                    call Main_Menu_Page()
                    BREAK
                ENDIF
                CLOSEFILE "ppe.txt"
            ELSE
                IF (option == "")THEN
                    call Main_Menu_Page()
                    ENDDO
                ELSE
                    Print"Invalid input! Please try again!"
                    Prompt user
                ENDIF
            ENDIF
        ENDIF
    ENDDO
END

#Search Item Inventory for printing list
FUNCTION Search_Item_Page()
BEGIN
    DECLARE item_code,cont
    DOWHILE (condition == TRUE)
        Print""
        OPENFILE "distribution.txt" FOR READ AS myFile
        Print"Search Item by respective item code: "
        Read item_code
        item_code := upper(item_code)
        IF ((item_code == "HC")OR(item_code == "FS")OR(item_code == "MS")OR(item_code == "GL")OR(item_code == "GW")OR(item_code == "SC"))THEN
            Print"Search done!"
            ASSIGN EMPTY LIST TO showlist
            ASSIGN EMPTY LIST TO display
            LOOP line IN myFile
                counter := 0
                ASSIGN SPLIT(line,",") TO L
                IF (L[1] == item_code)THEN
                    ASSIGN L[0] TO hoscode
                    ASSIGN L[2] TO quantity
                    OPENFILE "distribution.txt" FOR READ AS myFiles
                    LOOP lines IN myFiles
                        ASSIGN SPLIT(lines,",") TO J
                        IF ((J[0] == hoscode)AND(J[1] == item_code))THEN
                            counter := counter + 1
                            IF (counter > 1)THEN
                                DECLARE quantity : INTEGER
                                DECLARE J[2] : INTEGER
                                quantity = quantity + J[2]
                            ENDIF
                        ENDIF
                        NEXT lines
                    ENDLOOP
                    x := 1
                    LOOP Str IN showlist
                        ASSIGN SPLIT(Str,",") TO K
                        IF (K[0] == hoscode)THEN
                            x := 0
                            BREAK
                        ENDIF
                        NEXT Str
                    ENDLOOP
                    IF (x == 1)THEN
                        APPEND hoscode+","+item_code+","+str(quantity) TO showlist
                    ENDIF
                ENDIF
                NEXT line
            ENDLOOP
            Print"ITEM CODE: ",item_code
            Print"'{:<15s} {:<15s} {:<20s}'.format('Hospital Code', 'Item Code', 'Stock Quantity(boxes)')"
            Print"-------------   ---------       ---------------------"
            LOOP items IN showlist
                ASSIGN RSTRIP(items,"") TO items
                ASSIGN SPLIT(items,",") TO items
                APPEND items TO display
                NEXT items
            ENDLOOP
            LOOP line IN display
                Print"'{:<15s} {:<15s} {:<20s}'.format(line[0], line[1], str(line[2]))"
                NEXT line
            ENDLOOP
            CLOSEFILE "distribution.txt"
            Print"Press <ANY or ENTER> to continue or 'X' to end: "
            Read cont
            Print""
            IF ((cont == 'x')OR(cont == 'X'))THEN
                call Main_Menu_Page()
                BREAK
            ENDIF
        ELSE
            Print"Invalid item code! Please try again!"
            Prompt user
        ENDIF
    ENDDO
END

#REAL PROGRAM LAUNCH
PROGRAM PPE
BEGIN
    call Start_Up_Page()
END
