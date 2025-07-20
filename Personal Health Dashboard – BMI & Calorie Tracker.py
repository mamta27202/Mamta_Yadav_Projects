import tkinter as tk
from tkinter import messagebox

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal (Healthy)"
    elif 25 <= bmi < 30:
        return "Overweight"
    elif 30 <= bmi < 35:
        return "Obese Class I"
    elif 35 <= bmi < 40:
        return "Obese Class II"
    else:
        return "Obese Class III"

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100  # convert cm to meters
        bmi = weight / (height ** 2)
        category = interpret_bmi(bmi)
        bmi_result_label.config(text=f"BMI: {bmi:.2f} ({category})")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

def calculate_calories():
    try:
        age = int(age_entry.get())
        gender = gender_var.get()
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        activity = activity_var.get()

        # BMR Calculation using Mifflin-St Jeor Equation
        if gender == "Male":
            bmr = 10 * weight + 6.25 * height - 5 * age + 5
        else:
            bmr = 10 * weight + 6.25 * height - 5 * age - 161

        # Activity multipliers
        activity_levels = {
            "Sedentary": 1.2,
            "Lightly Active": 1.375,
            "Moderately Active": 1.55,
            "Very Active": 1.725,
            "Extra Active": 1.9
        }

        calories = bmr * activity_levels[activity]
        calorie_result_label.config(text=f"Estimated Daily Calories: {int(calories)} kcal")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

root = tk.Tk()
root.title("Personal Health Dashboard")
root.geometry("400x500")
root.config(bg="#F4F4F4")

# Title
tk.Label(root, text="BMI & Calorie Tracker", font=("Times New Roman", 16, "bold"), bg="#F4F4F4").pack(pady=10)

# Age
tk.Label(root, text="Age:", bg="#F4F4F4").pack()
age_entry = tk.Entry(root)
age_entry.pack()

# Gender
tk.Label(root, text="Gender:", bg="#F4F4F4").pack()
gender_var = tk.StringVar(value="Male")
tk.OptionMenu(root, gender_var, "Male", "Female").pack()

# Height
tk.Label(root, text="Height (cm):", bg="#F4F4F4").pack()
height_entry = tk.Entry(root)
height_entry.pack()

# Weight
tk.Label(root, text="Weight (kg):", bg="#F4F4F4").pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

# Activity Level
tk.Label(root, text="Activity Level:", bg="#F4F4F4").pack()
activity_var = tk.StringVar(value="Sedentary")
tk.OptionMenu(root, activity_var, "Sedentary", "Lightly Active", "Moderately Active", "Very Active", "Extra Active").pack()

# Buttons
tk.Button(root, text="Calculate BMI", command=calculate_bmi, bg="#F4F4F4", width=20).pack(pady=10)
bmi_result_label = tk.Label(root, text="", font=("Times New Roman", 12), bg="#F4F4F4")
bmi_result_label.pack()

tk.Button(root, text="Calculate Calories", command=calculate_calories, bg="#F4F4F4", width=20).pack(pady=10)
calorie_result_label = tk.Label(root, text="", font=("Times New Roman", 12), bg="#F4F4F4")
calorie_result_label.pack()

root.mainloop()
