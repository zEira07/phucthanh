names = set()

while True:
    name = input("Enter name (empty to quit): ")
    
    if name == "":
        break
    
    if name not in names:
        print("New name")
        names.add(name)
    else:
        print("Existing name")

print("\nNames entered:")

for name in names:
    print(name)