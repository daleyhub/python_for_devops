import sys

type = sys.argv[1]

if type == "t2.micro":
    print("Yes, you can create this instance type and it would cost you 7 dollars.")

elif type == "t2.medium":
    print("Yes you can create this instance type and it would cost you 17 dollars.")    

elif type == "t2.large":
    print("Yes you can create this instance type and it would cost you 27 dollars.")   

elif type == "t4.large":
    print("Yes you can create this instance type and it would cost you 37 dollars.")       

else: 
    print("Please input a valid instance type.")    