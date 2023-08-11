import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3 as sql

# Function to add a task to the list
def add_task():
    task_text = task_entry.get()
    if len(task_text) == 0:
        messagebox.showinfo('Error', 'Field is Empty.')
    else:
        tasks.append(task_text)
        the_cursor.execute('insert into tasks values (?)', (task_text,))
        update_task_list()
        task_entry.delete(0, 'end')

# Function to update the list of tasks in the list box
def update_task_list():
    clear_task_list()
    for task in tasks:
        task_listbox.insert('end', task)

# Function to delete a task from the list
def delete_task():
    try:
        selected_task = task_listbox.get(task_listbox.curselection())
        if selected_task in tasks:
            tasks.remove(selected_task)
            update_task_list()
            the_cursor.execute('delete from tasks where title = ?', (selected_task,))
    except:
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')

# Function to delete all tasks from the list
def delete_all_tasks():
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')
    if message_box:
        tasks.clear()
        the_cursor.execute('delete from tasks')
        update_task_list()

# Function to clear the list
def clear_task_list():
    task_listbox.delete(0, 'end')

# Function to close the application
def close():
    guiWindow.destroy()

# Function to retrieve data from the database
def retrieve_database():
    tasks.clear()
    for row in the_cursor.execute('select title from tasks'):
        tasks.append(row[0])

if __name__ == "__main__":
    guiWindow = tk.Tk()
    guiWindow.title("To-Do List Manager")
    guiWindow.geometry("500x450+750+250")
    guiWindow.resizable(0, 0)
    guiWindow.configure(bg="light blue")  # Change background color

    the_connection = sql.connect('listOfTasks.db')
    the_cursor = the_connection.cursor()
    the_cursor.execute('create table if not exists tasks (title text)')

    tasks = []

    header_frame = tk.Frame(guiWindow, bg="light blue")  # Change background color
    functions_frame = tk.Frame(guiWindow, bg="light blue")  # Change background color
    listbox_frame = tk.Frame(guiWindow, bg="light blue")  # Change background color

    header_frame.pack(fill="both")
    functions_frame.pack(side="left", expand=True, fill="both")
    listbox_frame.pack(side="right", expand=True, fill="both")

    header_label = ttk.Label(
        header_frame,
        text="The To-Do List",
        font=("Arial", 30),  # Change font
        background="light blue",  # Change background color
        foreground="#8B4513"
    )
    header_label.pack(padx=20, pady=20)

    task_label = ttk.Label(
        functions_frame,
        text="Enter the Task:",
        font=("Arial", 11, "bold"),  # Change font
        background="light blue",  # Change background color
        foreground="#000000"
    )
    task_label.place(x=30, y=40)

    task_entry = ttk.Entry(
        functions_frame,
        font=("Arial", 12),  # Change font
        width=18,
        background="#FFF8DC",
        foreground="#A52A2A"
    )
    task_entry.place(x=30, y=80)

    add_button = ttk.Button(
        functions_frame,
        text="Add Task",
        width=24,
        command=add_task
    )

    del_button = ttk.Button(
        functions_frame,
        text="Delete Task",
        width=24,
        command=delete_task
    )

    del_all_button = ttk.Button(
        functions_frame,
        text="Delete All Tasks",
        width=24,
        command=delete_all_tasks
    )

    exit_button = ttk.Button(
        functions_frame,
        text="Exit",
        width=24,
        command=close
    )

    add_button.place(x=30, y=120)
    del_button.place(x=30, y=160)
    del_all_button.place(x=30, y=200)
    exit_button.place(x=30, y=240)

    task_listbox = tk.Listbox(
        listbox_frame,
        width=26,
        height=13,
        selectmode='SINGLE',
        background="#FFFFFF",
        foreground="#000000",
        selectbackground="#CD853F",
        selectforeground="#FFFFFF"
    )
    task_listbox.place(x=10, y=20)

    retrieve_database()
    update_task_list()
    guiWindow.mainloop()

    the_connection.commit()
    the_cursor.close()
