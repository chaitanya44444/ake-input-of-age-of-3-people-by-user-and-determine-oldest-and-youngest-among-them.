age1=int(input("write an age"))
age2=int(input("write another age"))
age3=int(input("write another age"))

if age1>=age2>=age3:
    print(age1,"has the highest age") 
elif age2>=age3:
    print(int(age2),"has the highest age")
else:
    print(age3," is the oldest age out of the inputs")
