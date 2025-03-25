import csv
with open ("iit2024.csv" , "r") as a:
    b=csv.reader(a)
    s=[]
    for x in b:
       
        s.append(x[1])
        j=set(s)
        k=list(j)
    for i in k:
        print(i , end='\n')
