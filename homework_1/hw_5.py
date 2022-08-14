coming = int(input("Enter your coming:"))
cost = int(input("Enter your cost: "))
staff = int(input("Numbers of staff: "))
profit = coming - cost
cost_effect = profit / cost
if profit > 0:
    print(f"Congratulation, your profit = {profit} $")
    print(f"Cost_effect = {cost_effect:1} %")
    print(f"Profit for per staff = {profit / staff:2} $")
elif profit < 0:
    print(f"Sorry, your profit = {profit} $, Try your best")
else:
    print(f"Well")
