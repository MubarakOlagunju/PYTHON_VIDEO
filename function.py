#ADVANCED SIMPLE INTEREST CALCULATOR

print("--- Advanced Simple Interest Calculator ---")

def calculate_si(principal, rate, time):
    si = (principal * rate * time)/100
    return si

try:
    principal = int(input("Enter principal amount: "))
    rate = int(input("Enter rate(%): "))
    time = int(input("Enter time: "))

    result = calculate_si(principal, rate, time)
    print("Simple Interest is: ", result)
    
except ValueError:
    print("Enter a valid number!")