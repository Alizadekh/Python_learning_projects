salesperson_revenue = {
    "Aykhan": 0,
    "Famil": 0,
    "Ali": 0,
    "Amrah": 0,
}

def enter_revenue(name,revenue):
    global salesperson_revenue
    salesperson_revenue[name] += revenue

while True:
    name = input('Employee name: ')
    if name=="quit":
        break
    revenue = int(input("Enter revenue: "))
    enter_revenue(name,revenue)
    print(f"{name}'s revenue is {salesperson_revenue[name]}")

print(salesperson_revenue)