import tkinter
import tkinter.messagebox
import pickle   #For saving

#Screen
root = tkinter.Tk()
root.title("To-Do App")

#Add button Function
def add_task():
    task = entry_task.get()
    if task!='':
        list_box_task.insert(tkinter.END , task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title='Warning',message='You must enter task')

#Delete button Function
def delete_task():
    try: #The try block lets you test a block of code for errors.
        task_index = list_box_task.curselection()[0]#curselection - current task
        list_box_task.delete(task_index)
    except: #The except block lets you handle the error.
        tkinter.messagebox.showwarning(title='Warning', message='You must select a task')

#load Button Function
def load_task():
    try:
        tasks = pickle.load(open(r'C:\Users\ADHYAN\Desktop\Your Tasks.txt', "rb"))
        for tasks in tasks:
            list_box_task.insert(tkinter.END, tasks)
    except:
        tkinter.messagebox.showwarning(title='Warning', message="can't find Tasks.txt file")



#Save Button Function
def save_task():
    tasks = list_box_task.get(0,list_box_task.size())
    pickle.dump(tasks,open(r'C:\Users\ADHYAN\Desktop\Your Tasks.txt',"wb"))

# Creating GUI
#Frame
frame = tkinter.Frame(root)
frame.pack()

#Screen
list_box_task = tkinter.Listbox(frame,height=10, width=54 , bg = '#91cdf2')#Displaying screen
list_box_task.pack(side = tkinter.LEFT)

#Scroll - Bar
scroll_bar = tkinter.Scrollbar(frame)
scroll_bar.pack(side = tkinter.RIGHT, fill = tkinter.Y)# Y means that it should expand only vertically.

list_box_task.config(yscrollcommand = scroll_bar.set)
scroll_bar.config(command = list_box_task.yview)

#Entry Option
entry_task = tkinter.Entry(root, width = 54 , bg = '#a8e1ff')  #For Entry
entry_task.pack()

#Buttons -
#Add
Button_add = tkinter.Button(root,text = "Add task",width = 48,bg = '#039dfc',fg = '#f5fcfc',command = add_task)
Button_add.pack()

#Delete
Button_del = tkinter.Button(root,text = "Delete task",width = 48,bg = '#039dfc',fg = '#f5fcfc',command = delete_task)
Button_del.pack()

Button_load = tkinter.Button(root,text = "Load tasks",width = 48,bg = '#039dfc',fg = '#f5fcfc' ,command = load_task)
Button_load.pack()

Button_save = tkinter.Button(root,text = "Save task",width = 48,bg = '#039dfc',fg = '#f5fcfc',command = save_task)
Button_save.pack()
root.mainloop()