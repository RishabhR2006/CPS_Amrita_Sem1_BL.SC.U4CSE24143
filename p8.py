def readfile():
    f = open("Paragraph.txt",'r')
    text = f.read()
    f.close()
    ca=0
    cdot=0
    c9=0
    for i in text:
        if i=='a':
            ca=ca+1
        elif i=='.':
            cdot=cdot+1
        elif i=='9':
            c9=c9+1
    print("Number of a = ", ca)
    print("Number of . = ",cdot)
    print("Number of 9 = ",c9)

readfile()
