def readfile():
    f=open("Notice.txt",'r')
    text=f.read()
    f.close()
    
    words=text.split()
    print("Total number of words = ",len(words))

    print("The words endling with t are: ")
    for i in words:
        if i[-1]=='t':
            print(i)

    c4=0
    for i in words:
        if len(i)<4:
            c4=c4+1
    print("Number of words with less than 4 characters=",c4)

readfile()
