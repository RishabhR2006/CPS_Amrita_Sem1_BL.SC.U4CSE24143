def Push():
    SL_NO=int(input("Enter serial number: "))
    GName=input("Enter Name of Garment: ")
    Quantity=int(input("Enter quantity: "))
    Price=float(input("Enter price: "))
    stack.append([SL_NO, GName, Quantity, Price])

def Pop():
    if len(stack)==0:
        print("Stack empty!")
    else:
        data=stack.pop()
        print("Serial No:", data[0])
        print("Name of Garment:", data[1])
        print("Quantity:", data[2])
        print("Price:", data[3])

def Display():
    print("The contents of stack are:")
    for i in stack:
        print(i)

stack=[]
while True:
    print("Press 1 to push an element!")
    print("Press 2 to pop an element!")
    print("Press 3 to display all the elements!")
    print("Press 0 to exit the program!")
    ch=int(input("Enter your choice:"))
    if ch==1:
        Push()
    elif ch==2:
        Pop()
    elif ch==3:
        Display()
    elif ch==0:
        print("Thank you... Exiting...")
        break
    else:
        print("Wrong input!")
