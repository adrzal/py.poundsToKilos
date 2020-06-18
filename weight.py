weight = input("Weight: ")
unit = input("(L)bs or (K)g: ")
if unit.lower() == "k":
    print(f'You are {float(weight) * 2.204} pounds')
elif unit.lower() == "l":
    print(f'You are {float(weight) * 0.45359237} kilos')