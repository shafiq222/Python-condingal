actual_cost=float(input("Enter your money"))
sale_amount=float(input("Enter more money"))

if sale_amount > actual_cost:
    profit=sale_amount-actual_cost
    print("total profit is",profit) 
else:
    print("no profit")