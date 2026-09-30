while True:

    python=int(input("Enter marks of python: "))
    database=int(input("Enter marks of database: "))
    programming=int(input("Enter marks of programming: "))

    print("To enter student marks: Type 1")
    print("To display average marks: Type 2")
    print("To display highest marks: Type 3")
    print("To display lowest marks: Type 4")
    print("To display result marks: Type 5")
    print("To exit: Type 6")
    
    choice=input("Enter your choice:")
    print()

    match choice:
        case '1':
             

            print("\nYou have entered:\n")
            print(f"Python={python}\nDatabase={database}\nProgramming={programming}\n")
        case '2':
             
            average_marks=(python+database+programming)/3
            print(f"\nAverage marks: {average_marks}\n")
        case '3':
             

            temp= python if python>database else database
            highest_marks= temp if temp>programming else programming
            print(f"\nHighest marks: {highest_marks}\n")
        case '4':
            

            temp= python if python<database else database
            lowest_marks= temp if temp<programming else programming
            print(f"\nLowest marks: {lowest_marks}\n")
        case '5':
             
            
            percentage=((python+database+programming)/3)*100
           
            print("\nStudent result is: ")
            if(python>=40 and database>=40 and programming>=40 and percentage>=50):
                print(f"Student status:pass\n")
                
            else:
                print(f"Student status:fail\n")
                
        case '6': break
