def hemoglobin_check():
    sex = input("Enter biological sex (male/female): ").lower()
    hb = float(input("Enter hemoglobin value (g/l): "))

    if sex == "female":
        if hb < 117:
            print("Hemoglobin level is low.")
        elif hb <= 155:
            print("Hemoglobin level is normal.")
        else:
            print("Hemoglobin level is high.")
    elif sex == "male":
        if hb < 134:
            print("Hemoglobin level is low.")
        elif hb <= 167:
            print("Hemoglobin level is normal.")
        else:
            print("Hemoglobin level is high.")
    else:
        print("Invalid sex input.")
hemoglobin_check()