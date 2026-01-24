import math

def pizza_unit_price(diameter_cm, price_usd):
    radius_m = (diameter_cm / 100) / 2
    area_m2 = math.pi * radius_m ** 2
    return price_usd / area_m2


def compare_pizzas():
    diameter1 = float(input("Enter diameter of pizza 1 (cm): "))
    price1 = float(input("Enter price of pizza 1 (USD): "))

    diameter2 = float(input("Enter diameter of pizza 2 (cm): "))
    price2 = float(input("Enter price of pizza 2 (USD): "))

    unit_price1 = pizza_unit_price(diameter1, price1)
    unit_price2 = pizza_unit_price(diameter2, price2)

    if unit_price1 < unit_price2:
        print("Pizza 1 provides better value for money.")
    elif unit_price2 < unit_price1:
        print("Pizza 2 provides better value for money.")
    else:
        print("Both pizzas provide the same value for money.")
compare_pizzas()
compare_pizzas()