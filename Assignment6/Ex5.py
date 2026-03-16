def remove_odds(numbers):
    result = []
    
    for n in numbers:
        if n % 2 == 0:
            result.append(n)
    
    return result


def main():
    original = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    filtered = remove_odds(original)

    print("Original list:", original)
    print("List without odd numbers:", filtered)


main()