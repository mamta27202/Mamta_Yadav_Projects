import tkinter as tk
from tkinter import messagebox
import json

# Sample quiz data
quiz_data = [
    {"question": "What is the capital of France?", "options": ["Paris", "Rome", "Berlin", "London"], "answer": "Paris"},
    {"question": "Which element has the atomic number 1?", "options": ["He", "O", "H", "Li"], "answer": "H"},
    {"question": "Python is a...", "options": ["Snake", "Language", "Food", "Drink"], "answer": "Language"}
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application")
        self.root.geometry("400x300")
        self.qn = 0
        self.score = 0
        self.question_label = tk.Label(root, text="", font=("Times New Roman", 14), wraplength=350)
        self.question_label.pack(pady=20)
        self.var = tk.StringVar()
        self.options = [tk.Radiobutton(root, text="", variable=self.var, value="", font=("Arial", 12)) for _ in range(4)]
        for opt in self.options:
            opt.pack(anchor="w")
        tk.Button(root, text="Next", command=self.next_question).pack(pady=10)
        self.load_question()

    def load_question(self):
        self.var.set(None)
        q = quiz_data[self.qn]
        self.question_label.config(text=q["question"])
        for i, option in enumerate(q["options"]):
            self.options[i].config(text=option, value=option)

    def next_question(self):
        if self.var.get() == quiz_data[self.qn]["answer"]:
            self.score += 1
        self.qn += 1
        if self.qn < len(quiz_data):
            self.load_question()
        else:
            messagebox.showinfo("Quiz Complete", f"Your score: {self.score}/{len(quiz_data)}")
            self.root.quit()

root = tk.Tk()
app = QuizApp(root)
root.mainloop()
