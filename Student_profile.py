import tkinter
from tkinter import messagebox
root = tkinter.Tk()
root.title("Student Profile")
root.geometry("400x300")

label = tkinter.Label(root, text="Enter your name:")
label.pack()
Name = tkinter.Entry(root)
Name.pack()


label = tkinter.Label(root, text="Enter your age:")
label.pack()
Age = tkinter.Entry(root)
Age.pack()



label = tkinter.Label(root, text="Enter your major:")
label.pack()
Major= tkinter.Entry(root)
Major.pack()


label = tkinter.Label(root, text="Enter your career goal:")
label.pack()
Career_Goal= tkinter.Entry(root)
Career_Goal.pack()




def get_student_info():
    messagebox.showinfo("Information", f"Hello {Name.get()}, you are {Age.get()} years old, majoring in {Major.get()}, and your career goal is to become a {Career_Goal.get()}.")

submit_btn = tkinter.Button(root, text="Submit", command=get_student_info, )
submit_btn.pack(pady=5)


def exit_program():
    exit_btn = tkinter.Button(root, text="Exit", command=exit_program)
    exit_btn.pack(pady=6)
    root.destroy
root.mainloop()