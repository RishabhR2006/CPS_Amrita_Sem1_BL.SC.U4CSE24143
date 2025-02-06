import pickle

def StoreComp():
    L=[]
    n=int(input("Enter number of Computer articles: "))
    for i in range(n):
        SLNo=int(input("Enter Serial Number: "))
        Particulars=input("Enter Particulars: ")
        Qty=int(input("Enter Quantity: "))
        Price=float(input("Enter Price: "))
        L.append([SLNo, Particulars, Qty, Price])

    f=open("Comp.dat",'wb')
    pickle.dump(L,f)
    f.close()

def DisplayComp():
    f=open("Comp.dat",'rb')
    L=pickle.load(f)
    for i in L:
        print("Serial Number: ",i[0])
        print("Particulars: ",i[1])
        print("Quantity: ",i[2])
        print("Price: ",i[3])
        print()
    f.close()

StoreComp()
DisplayComp()

