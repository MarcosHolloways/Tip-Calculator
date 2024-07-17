print("Welcome to the tip calculator.")
total = float(input("What was the total bill? "))
porcent = int(input ("What the percentage tip would you like to give? 10, 12 or 15 "))
people = int(input("how many people to spit the bill "))
pricewithouttip = (total/people) 
pricewithtip = ( pricewithouttip / 100 ) * porcent + pricewithouttip
print(f"Each person should pay: {(pricewithtip)}")
