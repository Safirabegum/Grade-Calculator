import tkinter
from tkinter import *

root = Tk()
root.title("Grade Calculator")
root.geometry("500x400")


def Calculation():
    try:
        english = int(englishentry.get())
        skills = int(analytical_skillentry.get())
        general = int(generalentry.get())

        total = english + skills + general
        avg = total / 3

        # Clear previous results
        total_label.config(text=f"Total: {total}")
        average_label.config(text=f"Average: {avg:.2f}")  # Display average with 2 decimal places

        if avg > 50:
            grade = "PASS"
        else:
            grade = "FAIL"
        grade_label.config(text=f"Grade: {grade}")

    except ValueError:
        # Handle the case where input is not a valid integer
        total_label.config(text="Please enter valid numbers")
        average_label.config(text="")
        grade_label.config(text="")


# Subject Labels
Label(root, text="English:", font="arial 10").place(x=50, y=20)
Label(root, text="Analytical Skill:", font="arial 10").place(x=50, y=70)
Label(root, text="General knowledge:", font="arial 10").place(x=50, y=120)

# Entry Widgets
englishentry = Entry(root, font="arial 15", width=15)
analytical_skillentry = Entry(root, font="arial 15", width=15)
generalentry = Entry(root, font="arial 15", width=15)

englishentry.place(x=250, y=20)
analytical_skillentry.place(x=250, y=70)
generalentry.place(x=250, y=120)

# Result Labels
total_label = Label(root, text="Total:", font="arial 10")
average_label = Label(root, text="Average:", font="arial 10")
grade_label = Label(root, text="Grade:", font="arial 10")

total_label.place(x=50, y=170)
average_label.place(x=50, y=210)
grade_label.place(x=50, y=250)

# Buttons
Button(root, text="Calculate", font="arial 15", bg="white", bd=10, command=Calculation).place(x=50, y=300)
Button(root, text="Exit", font="arial 15", bg="white", bd=10, width=8, command=root.destroy).place(x=250, y=300)

root.mainloop()
