# Slide Title: Matrix Calculator – Python GUI Project**
# ###  **Project Overview**
# A desktop application to perform key matrix operations using a graphical interface.
# ###  **Technologies Used**
# * Python
# * Tkinter (GUI)
# * NumPy (Matrix Calculations)
# ###  **Key Features**

# * Matrix Addition & Subtraction
# * User-friendly Entry Fields
# * Real-time Result Display
# * Error Handling for Invalid Input

# ###  **What I Learned**

# * GUI development with Tkinter
# * Matrix handling using NumPy
# * Error handling and user validation
# * Real-world use of scientific computing

# ###  **Use Case**

# Useful for students, teachers, or engineers needing quick and reliable matrix computations without coding.

import tkinter as tk
from tkinter import messagebox
import numpy as np

root = tk.Tk()
root.title("Visual Matrix Calculator")
root.geometry("600x450")

# Frames
matrix_frame1 = tk.Frame(root)
matrix_frame1.pack(pady=10)

matrix_frame2 = tk.Frame(root)
matrix_frame2.pack(pady=10)

result_frame = tk.Frame(root)
result_frame.pack(pady=10)

# Create matrix input fields
def create_matrix_input(rows, cols, frame):
    entries = []
    for i in range(rows):
        row_entries = []
        for j in range(cols):
            e = tk.Entry(frame, width=5)
            e.grid(row=i, column=j, padx=2, pady=2)
            row_entries.append(e)
        entries.append(row_entries)
    return entries

# Define matrices
matrix1_entries = create_matrix_input(2, 2, matrix_frame1)
matrix2_entries = create_matrix_input(2, 2, matrix_frame2)

# Read matrix from input fields
def read_matrix(entries):
    matrix = []
    for row in entries:
        row_values = []
        for e in row:
            value = e.get().strip()
            if value == "":
                raise ValueError("All matrix cells must be filled.")
            row_values.append(float(value))
        matrix.append(row_values)
    return np.array(matrix)

# Display result in GUI
def display_result(matrix):
    for widget in result_frame.winfo_children():
        widget.destroy()
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            label = tk.Label(result_frame, text=str(round(matrix[i][j], 2)), width=7)
            label.grid(row=i, column=j)

# Matrix operations
def add_matrices():
    try:
        m1 = read_matrix(matrix1_entries)
        m2 = read_matrix(matrix2_entries)
        result = m1 + m2
        display_result(result)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def subtract_matrices():
    try:
        m1 = read_matrix(matrix1_entries)
        m2 = read_matrix(matrix2_entries)
        result = m1 - m2
        display_result(result)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def multiplication_matrices():
    try:
        m1 = read_matrix(matrix1_entries)
        m2 = read_matrix(matrix2_entries)
        result = np.matmul(m1, m2)
        display_result(result)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def division_matrices():
    try:
        m1 = read_matrix(matrix1_entries)
        m2 = read_matrix(matrix2_entries)
        inv_m2 = np.linalg.inv(m2)
        result = np.matmul(m1, inv_m2)
        display_result(result)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def exponential_matrices():
    try:
        m1 = read_matrix(matrix1_entries)
        result = np.linalg.matrix_power(m1, 2)  # Power of 2, you can make it dynamic
        display_result(result)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Buttons
tk.Button(root, text="Add", command=add_matrices).pack(pady=5)
tk.Button(root, text="Subtract", command=subtract_matrices).pack(pady=5)
tk.Button(root, text="Multiply", command=multiplication_matrices).pack(pady=5)
tk.Button(root, text="Divide", command=division_matrices).pack(pady=5)
tk.Button(root, text="Power", command=exponential_matrices).pack(pady=5)

root.mainloop()