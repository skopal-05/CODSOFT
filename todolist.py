from tkinter import *
from tkinter import messagebox

task_list = []

num = 1

def NoInput() :
    if enterTaskField.get() == "" :
        messagebox.showerror("No task given")
        return 0
    return 1

def clear_taskNumberField() :
    taskNumberField.delete(0.0, END)

def clear_taskField() :
    enterTaskField.delete(0, END)

def insertTask():
    global num
    value = NoInput()
    if value == 0 :
        return
    task = enterTaskField.get() + "\n"
    task_list.append(task)
    TextArea.insert('end -1 chars', str(num) + ". " + task)
    num += 1
    clear_taskField()

def delete() :
    global num
    if len(task_list) == 0 :
        messagebox.showerror("No task")
        return
    number = taskNumberField.get(1.0, END)
    if number == "\n" :
        messagebox.showerror("input error")
        return
    else :
        task_no = int(number)
    clear_taskNumberField()
    task_list.pop(task_no - 1)
    num -= 1
    TextArea.delete(1.0, END)
    for i in range(len(task_list)) :
        TextArea.insert('end -1 chars', "[ " + str(i + 1) + " ] " + task_list[i])
 
if __name__ == "__main__" :
    gui = Tk()
    gui.configure(background = "cyan")
    gui.title("To Do List")
    gui.geometry("300x450")
    enterTask = Label(gui, text = "Enter  Task", bg = "light pink")
    enterTaskField = Entry(gui)
    Submit = Button(gui, text = "Submit", fg = "Black", bg = "green", command = insertTask)
    TextArea = Text(gui, height = 5, width = 25, font = "lucida 13")
    taskNumber = Label(gui, text = "Delete Task Number", bg = "blue")
    taskNumberField = Text(gui, height = 1, width = 2, font = "lucida 13")
    delete = Button(gui, text = "Delete", fg = "Red", bg = "black", command = delete)
    Exit = Button(gui, text = "Exit", fg = "white", bg = "black", command = exit)
    enterTask.grid(row = 0, column = 2)
    enterTaskField.grid(row = 1, column = 2, ipadx = 50)
    Submit.grid(row = 2, column = 2)
    TextArea.grid(row = 3, column = 2, padx = 10, sticky = W)
    taskNumber.grid(row = 4, column = 2, pady = 5)
    taskNumberField.grid(row = 5, column = 2)
    delete.grid(row = 6, column = 2, pady = 5)
    Exit.grid(row = 7, column = 2)
    gui.mainloop()
