#Electricity Bill calculator using if-elif-else
print("------ELectricity Bill Generator---------------")
units=int(input("Enter the number of units:"))
bill_for_f_100=units*5
bill_for_n_100=100*5 + (units-100)*7
bill_for_max_400units=100*5 + 100*7 + (units-200)*10
bill_for_above_400units=100*5 + 100*7 + 200*7 + (units-400)*12
if units<=100:
    print("Your Electricity bill is:",bill_for_f_100)
elif units>100 and units<=200:
    print("Your Electricity bill is:",bill_for_n_100)
elif units>200 and units<=400:
    print("Your Electricity bill is:",bill_for_max_400units)
elif units>400:
    print("Your electricity bill is:",bill_for_above_400units)
else:
    print("You have entered wrong value!")


 


































 