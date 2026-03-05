import re

def is_valid_course(code):
    pattern = r'^[A-Z]{2,3}[0-9]{3}$'
    return bool(re.match(pattern, code))


# Test
print(is_valid_course("TEC001"))  # True
print(is_valid_course("AU006"))   # True
print(is_valid_course("A1001"))   # False
print(is_valid_course("tec001"))  # False