glucose_range = range(80, 181)
bp_range = range(80, 131)
skin_range = range(20, 48)
insulin_range = range(90, 169)
bmi_range = range(30, 43)
age_range = range(30, 150)

# take input from user for the factors
glucose = int(input("Enter glucose level (80-180): "))
bp = int(input("Enter blood pressure (80-130): "))
skin_thickness = int(input("Enter skin thickness (20-47): "))
insulin = int(input("Enter insulin level (90-168): "))
bmi = int(input("Enter BMI (30-42): "))
age = int(input("Enter age (30 and above): "))

# check if the input values are within the defined ranges
if glucose not in glucose_range:
    print("Invalid glucose level")
elif bp not in bp_range:
    print("Invalid blood pressure")
elif skin_thickness not in skin_range:
    print("Invalid skin thickness")
elif insulin not in insulin_range:
    print("Invalid insulin level")
elif bmi not in bmi_range:
    print("Invalid BMI")
elif age not in age_range:
    print("Invalid age")
else:
    # check if the person is diabetic or not based on the given table
    if glucose > 150 and bp < 110 and skin_thickness > 40 and insulin < 120 and bmi < 35 and age > 35:
        print("The person is diabetic")
    elif glucose > 150 and bp > 120 and skin_thickness < 30 and insulin > 120 and bmi > 40 and age < 35:
        print("The person is not diabetic")
    elif glucose < 140 and bp > 120 and skin_thickness > 43 and insulin < 100 and bmi < 40 and age < 50:
        print("The person is diabetic")
    elif glucose < 130 and bp < 95 and skin_thickness < 32 and insulin > 135 and bmi < 38 and age < 70:
        print("The person is diabetic")
    elif glucose < 128 and bp > 125 and skin_thickness > 45 and insulin > 148 and bmi < 31 and age < 40:
        print("The person is not diabetic")
    elif glucose > 165 and bp > 125 and skin_thickness < 28 and insulin > 155 and bmi > 41 and age > 75:
        print("The person is diabetic")
    elif glucose > 178 and bp < 115 and skin_thickness > 38 and insulin < 95 and bmi == 42 and age < 78:
        print("The person is diabetic")
    else:
        print("The person is not diabetic")
