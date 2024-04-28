from tkinter import *
from tkinter import messagebox
import sqlite3 as sq


def add_task():
    word = txt_input.get()
    if len(word) == 0:
        messagebox.showinfo('Empty Entry', 'Enter task name')
    else:
        task.append(word)
        cur.execute('insert into tasks values (?)', (word,))
        update_list()
        txt_input.delete(0, 'end')


def update_list():
    clear_list()
    for i in task:
        lb_tasks.insert('end', i)


def delete_one():
    try:
        val = lb_tasks.get(lb_tasks.curselection())
        if val in task:
            task.remove(val)
            update_list()
            cur.execute('delete from tasks where title = ?', (val,))
    except:
        messagebox.showinfo('Cannot Delete', 'No Task Item Selected')


def delete_all():
    mb = messagebox.askyesno('Delete All', 'Are you sure?')
    if mb == True:
        while (len(task) != 0):
            task.pop()
        cur.execute('delete from tasks')
        update_list()


def clear_list():
    lb_tasks.delete(0, 'end')


def retrieve_db():
    while (len(task) != 0):
        task.pop()
    for row in cur.execute('select title from tasks'):
        task.append(row[0])


if __name__ == "__main__":
    root = Tk()
    root.title('To Do List App')
    root.geometry("250x450")
    root.resizable(False, False)

    # Establish connection with database
    conn = sq.connect('todo.db')
    cur = conn.cursor()

    cur.execute('create table if not exists tasks (title text)')

    task = []

    # Set Widgets
    lbl_title = Label(root, text='To Do List', font=('Helvetica', 18, 'bold'))
    lbl_task_show = Label(root, text='Enter task below :',
                          font=('Helvetica', 10))
    txt_input = Entry(root, width=25, bd="2", font="18")
    lb_tasks = Listbox(root, width=24, height=10,
                       selectmode='SINGLE', relief=RIDGE, bd="4", font="14")
    btn_add_task = Button(root, text='Add task', width=20,
                          command=add_task, relief=RIDGE)
    btn_del_one = Button(root, text='Delete', width=20,
                         relief=RIDGE, command=delete_one)
    btn_del_all = Button(root, text='Delete all', width=20,
                         relief=RIDGE, command=delete_all)
    btn_exit = Button(root, text='Exit', width=20, relief=RIDGE, command=exit)

    retrieve_db()
    update_list()

    # Place geometry
    lbl_title.place(x=60, y=5)
    lbl_task_show.place(x=70, y=45)
    txt_input.place(x=10, y=80)
    btn_add_task.place(x=50, y=115)
    btn_del_one.place(x=50, y=145)
    btn_del_all.place(x=50, y=175)
    btn_exit.place(x=50, y=205)
    lb_tasks.place(x=12, y=240)

    root.mainloop()

    conn.commit()
    cur.close()
