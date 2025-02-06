def readfile():
    f=open("report.txt",'r')
    Lines=f.readlines()
    f.close()

    print("Total number of lines = ",len(Lines))

    print("The lines starting with T are: ")
    for i in Lines:
        if i[0]=='T':
            print(i)

    cw=0
    for i in Lines:
        words=i.split()
        if len(words)<4:
            cw=cw+1
    print("Number of lines having less than 4 words = ", cw)

readfile()
    
    
