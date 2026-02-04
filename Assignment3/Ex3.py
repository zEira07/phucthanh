first = True
smallest = 0
largest = 0

while True:
    user_input = input("Enter a number: ")

    if user_input == "":
        break

    number = float(user_input)

    if first:
        smallest = number
        largest = number
        first = False
    else:
        if number < smallest:
            smallest = number
        if number > largest:
            largest = number

if not first:
    print("Smallest number:", smallest)
    print("Largest number:", largest)
