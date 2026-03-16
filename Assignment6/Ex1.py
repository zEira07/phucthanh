numbers = []

while True:
    value = input("Enter a number (empty to quit): ")
    
    if value == "":
        break
        
    numbers.append(float(value))

numbers.sort(reverse=True)

print("Five greatest numbers:")
for n in numbers[:5]:
    print(n)