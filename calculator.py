def calculator():
    print("...!!SIMPLE CALCULATOR!!...")
    num1=int(input("Enter number 1:"))
    operation=input("Enter any one operation (+,-,*,/):")
    num2=int(input("Enter number 2:"))
    if operation=="+":
        print(f"Addition of {num1} and {num2}=",num1+num2)
    elif operation=="-":
        print(f"Subtraction of {num1} and {num2}=", num1-num2)
    elif operation=="*":
        print(f"Mutltiplication of {num1} and {num2}=",num1*num2)
    elif operation=="/":
        if num2==0:
            print("Error,Division by Zero")
        else:
            print(f"Division of {num1} and {num2}=", num1/num2)
    else:
        print("Invalid Operation")
calculator()