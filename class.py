# CTE213 Project - Workshop Energy Cost Estimator
# Name: saviour jeremiah etim - ND2 Mechatronics YABATECH
#F/ND/24/3450003

def calc_kwh(power, hours):
    kwh = (power / 1000) * hours
    return kwh

def calc_cost(kwh, tariff):
    cost = kwh * tariff
    return cost

def energy_saving_status(power):
    if power > 1500:
        return "High power - Use PLC timer"
    elif power > 800:
        return "Medium power - Can use timer"
    else:
        return "Low power - OK"

print("Welcome to Workshop Energy Cost Estimator")
print("By Saviour jeremiah etim - CTE213")

machine_names = []
machine_power = []
machine_hours = []
machine_kwh = []

n = int(input("How many machines do you have in the workshop? "))
print("Okay, can you name them?")

for i in range(n):
    print("Enter the name for machine " + str(i + 1) + ":")
    name = input("Machine name: ")
    machine_names.append(name)

    p = float(input("Enter power of " + name + " in watts: "))
    machine_power.append(p)

    h = float(input("Enter hours " + name + " works per day: "))
    machine_hours.append(h)

    kwh = calc_kwh(p, h)
    machine_kwh.append(kwh)
    print("Okay, " + name + " recorded.")

print("Thank you. Now let us calculate the cost.")
tariff = float(input("Enter tariff per kWh in Naira: "))

total_kwh = 0
for k in machine_kwh:
    total_kwh = total_kwh + k

total_cost = calc_cost(total_kwh, tariff)

print("--- Result ---")
for i in range(n):
    print(machine_names[i] + " uses " + str(machine_kwh[i]) + " kWh per day")

print("Total daily kWh: " + str(total_kwh))
print("Daily cost: " + str(total_cost) + " Naira")

monthly_kwh = total_kwh * 30
monthly_cost = monthly_kwh * tariff
print("Monthly kWh (30 days): " + str(monthly_kwh))
print("Monthly cost: " + str(monthly_cost) + " Naira")

print("Largest daily kWh: " + str(max(machine_kwh)))

count = 0
for p in machine_power:
    if p > 1000:
        count = count + 1

print("Machines above 1000W: " + str(count))

if total_kwh > 20:
    print("High energy workshop")
elif total_kwh > 10:
    print("Medium energy workshop")
else:
    print("Low energy workshop")

print("--- My Own Twist: PLC Energy Saving ---")
for i in range(n):
    status = energy_saving_status(machine_power[i])
    print(machine_names[i] + ": " + status)

if count > 0:
    print("You can save energy if you OFF high power machines for 4 hours with PLC timer")