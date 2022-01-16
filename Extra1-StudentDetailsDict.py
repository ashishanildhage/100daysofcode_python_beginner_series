#Build a Students Details database System using purely dictionaries
main_database={}
print("""
    Welcome to SDMS!
    The Only Student Database Management System you will ever need!
    Its Fast, efficient and handy.
    Have Fun
                                    - Ashish Anil Dhage
""")
def inputter():
    """Takes input from the user to fill the database of student details"""
    database={}
    print("Enter the Students details : ")
    roll=input("> Roll number - ")
    database["roll"]=roll
    database["name"]=input("> Name - ").title()
    #Marks 1
    looper=True
    while looper:
        try:
            database["m1"]=float(input("> 1st subject Marks - ")) or 0
            if 0<=database["m1"]<=100: looper=False
            else: print("Please enter between 0 and 100")    
        except: print("Please enter a number")
    #Marks 2
    looper=True
    while looper:
        try:
            database["m2"]=float(input("> 2nd subject Marks - ")) or 0
            if 0<=database["m1"]<=100: looper=False
            else: print("Please enter between 0 and 100")    
        except: print("Please enter a number")
    #Marks 3
    looper=True
    while looper:
        try:
            database["m3"]=float(input("> 3rd subject Marks - ")) or 0
            if 0<=database["m1"]<=100: looper=False
            else: print("Please enter between 0 and 100")    
        except: print("Please enter a number")

    database["address"]=input("> Address - ")
    fake=True
    while fake:
        contactno=input("> Contact No - ")
        if len(contactno)!=10:
            print("Invalid Phone Number")
        else:    
            database["contactno"]=contactno
            fake=False
    database["total"]=round(database["m1"]+database["m2"]+database["m3"],2)
    ptr=round(database["total"]/3,2)
    database["ptr"]=ptr
    if ptr>=90:
        results="Distinction"
    elif 80<=ptr<90:
        results="First Class"
    elif 60<=ptr<80:
        results="Second Class"
    elif 40<=ptr<60:
        results="Third Class"
    elif ptr<40:
        results="Fail"
    database["results"]=results
    main_database["Stud"+roll]=database

def displayer():
    """Displays database of student details by printing one below the other"""
    for student in main_database:
        for columns in main_database[student]:
            #main_database={Stud1:{roll:1,name:ash........}}
            #student=Stud1
            #main_database[student]={roll:1,......}=detail
            #columns=roll
            #detail[columns]=1,...
            print(f"{columns} - {main_database[student][columns]}")
        print()

def searcher():
    """Takes roll number input from the user to search for student details in database"""
    search="Stud"+input("Enter Roll No of Student to be searched : ")
    try:
        print(main_database[search])
    except: 
        print("Invalid Roll Number")

def modifier():
    """Takes roll number input from the user to modify the student details in database"""
    modify="Stud"+input("Enter Roll No of Student to be modified : ")
    print("""
        1 Marks
        2 Address
        3 Contact Number""")
    modify_detail=int(input("Choose the Detail : "))
    try:
        if modify_detail==1:
            main_database[modify]["m1"]=float(input("> 1st subject Marks - ")) or 0
            main_database[modify]["m2"]=float(input("> 2nd subject Marks - ")) or 0
            main_database[modify]["m3"]=float(input("> 3rd subject Marks - ")) or 0
            main_database[modify]["total"]=round(main_database[modify]["m1"]+main_database[modify]["m2"]+main_database[modify]["m3"],2)
            ptr=round(main_database[modify]["total"]/3,2)
            main_database[modify]["ptr"]=ptr
            if ptr>=90:
                results="Distinction"
            elif 80<=ptr<90:
                results="First Class"
            elif 60<=ptr<80:
                results="Second Class"
            elif 40<=ptr<60:
                results="Third Class"
            elif ptr<40:
                results="Fail"
            main_database[modify]["results"]=results
        elif modify_detail==2:
            main_database[modify]["address"]=input("> Address -")
        elif modify_detail==3:
            main_database[modify]["contactno"]=input("> Contact Number -")
        else :
            print("Invalid Choice")   
    except: 
        print("Invalid Roll Number")

def deleter():
    """deletes a student's details from the database"""
    junk="stud"+input("Enter Roll No of Student to be deleted : ")
    try:
        del main_database[junk]
    except KeyError: 
        print("Invalid Roll Number")


exitter=True
while exitter:
    print("""
        1 Add Student
        2 Display All Students
        3 Search for a Student
        4 Modify the Student Details
        5 Delete the Student Details
        6 Exit
        """)
    try:
        choice=int(input("Choose the Operation : "))
        if choice==1:
            inputter()
        elif choice==2:
            displayer()
        elif choice==3:
            searcher()
        elif choice==4:
            modifier()
        elif choice==5:
            deleter()
        elif choice==6:
            exitter=False
        else:
            print("Invalid Choice")
    except:
        print("Invalid Input, only enter 1,2,3,4,5 or 6!")

#Done!






