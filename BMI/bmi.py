def calculate_bmi(height, weight, is_metric=True):
    try:
        factor = 1 if is_metric else 703
        return round(weight / (height ** 2) * factor, 2)
    except ZeroDivisionError:
        return None

def interpret_bmi(bmi):
    if bmi is None:
        return "Invalid input. Height should be greater than 0."

    categories = [
        (0, 16, "Severely underweight"),
        (16, 16.9, "Underweight"),
        (17, 18.4, "Mildly underweight"),
        (18.5, 24.9, "Normal weight"),
        (25, 29.9, "Overweight"),
        (30, 34.9, "Obesity Class 1 (Moderate)"),
        (35, 39.9, "Obesity Class 2 (Severe)"),
        (40, float('inf'), "Obesity Class 3 (Very severe or morbidly obese)")
    ]

    for min_value, max_value, label in categories:
        if min_value <= bmi < max_value:
            return f"Your BMI is {bmi}, you are {label}."

def display_bmi_chart(categories):
    print("BMI Categories:")
    for min_value, max_value, label in categories:
        print(f"{min_value}-{max_value}: {label}")

def convert_units(height, weight, is_metric):
    if is_metric:
        return height * 3.28084, weight * 2.20462
    else:
        return height / 3.28084, weight / 2.20462

def get_user_input():
    try:
        is_metric = input("Choose units (1 for metric, 0 for imperial): ").strip() == "1"
        height_unit = "meters" if is_metric else "feet"
        weight_unit = "kilograms" if is_metric else "pounds"
        height = float(input(f"Enter your height in {height_unit}: "))
        weight = float(input(f"Enter your weight in {weight_unit}: "))
        return height, weight, is_metric
    except ValueError:
        return None, None, is_metric

def main():
    categories = [  # Define 'categories' here
        (0, 16, "Severely underweight"),
        (16, 16.9, "Underweight"),
        (17, 18.4, "Mildly underweight"),
        (18.5, 24.9, "Normal weight"),
        (25, 29.9, "Overweight"),
        (30, 34.9, "Obesity Class 1 (Moderate)"),
        (35, 39.9, "Obesity Class 2 (Severe)"),
        (40, float('inf'), "Obesity Class 3 (Very severe or morbidly obese)")
    ]

    while True:
        print("BMI Calculator Menu:")
        print("1. Calculate BMI")
        print("2. Convert Units")
        print("3. Exit")
        
        choice = input("Select an option (1/2/3): ").strip()
        
        if choice == "1":
            height, weight, is_metric = get_user_input()
            if height is None or weight is None:
                print("Invalid input. Please enter valid numerical values for height and weight.")
            else:
                bmi = calculate_bmi(height, weight, is_metric)
                result = interpret_bmi(bmi)
                print(result)
                display_bmi_chart(categories)  # Pass 'categories' here
        elif choice == "2":
            height, weight, is_metric = get_user_input()
            if height is None or weight is None:
                print("Invalid input. Please enter valid numerical values for height and weight.")
            else:
                new_height, new_weight = convert_units(height, weight, is_metric)
                height_unit = "feet" if is_metric else "meters"
                weight_unit = "pounds" if is_metric else "kilograms"
                print(f"Height: {new_height:.2f} {height_unit} / {height:.2f} {height_unit}")
                print(f"Weight: {new_weight:.2f} {weight_unit} / {weight:.2f} {weight_unit}")
        elif choice == "3":
            print("Exiting BMI Calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1/2/3).")

if __name__ == "__main__":
    main()
