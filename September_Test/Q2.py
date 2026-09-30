print("We are here to make a Simple Calculator")
num1=float(input("Enter the First Number:"))
num2=float(input("Enter the Second Number:"))
operator=input("Enter the operator(+,-,*,%,/):")

match operator:
    case '+':
        print(f"The addition of two numbers are:{num1+num2}")
    case'-':
        print(f"The subtraction of two numbers are:{num1-num2}")
    case'*':
            print(f"The subtraction of two numbers are:{num1*num2}")
    case'%':
            print(f"The subtraction of two numbers are:{num1%num2}")
    case'/':
            print(f"The subtraction of two numbers are:{num1/num2}")    