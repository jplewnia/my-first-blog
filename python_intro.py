print('Hello, djangogirls')
def vergleich(a,b):
    if a < b:
        print("jawoll")
    elif a==b:
        print("whatever")    
    else:
        print("och nee")
vergleich(5,2)

def hi(names= []):
    for name in names:
        print ("Hi "+ name)
hi(["Lisa", "Marie", "Sarah"]) 

for i in range(1,6):
    print(i)