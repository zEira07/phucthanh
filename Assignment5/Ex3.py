import re

def sum_numbers(text):
    return sum(map(int, re.findall(r'\d+', text)))


# Example
text = "Today is January 16, 2025. The temperature is 11 degrees Celsius."
print(sum_numbers(text))