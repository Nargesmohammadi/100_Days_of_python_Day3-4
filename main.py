print("Welcome to Python pizza deliveries!")
size = input("what size pizza do you want? S , M , L ?")
add_pepperoni = input("do you want pepperoni? Y , N ?")
extra_cheese = input("do you want extra cheese? Y , N ?")
bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is ${bill}")
