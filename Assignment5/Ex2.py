import re

def is_hex_color(color):
    pattern = r'^#[0-9A-Fa-f]{6}$'
    return bool(re.match(pattern, color))


# Test
print(is_hex_color("#FFAA00"))  # True
print(is_hex_color("#ff00cc"))  # True
print(is_hex_color("#123ABZ"))  # False
print(is_hex_color("FFAA00"))   # False