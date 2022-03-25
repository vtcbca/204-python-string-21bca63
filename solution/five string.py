
l=[]
count=0
def list(l):
    for i in range(5):
        s=input("Enter the string:")
        l.append(s)
list(l)
def evenlenth(l):
    for i in l:
        count=0
        for j in i:
            count=count+1
        if(count%2==0):
            print("The list is {} and its lemnth is {}.".format(i,count))
evenlenth(l)
