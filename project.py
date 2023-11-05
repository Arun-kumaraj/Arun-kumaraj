import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END,task)
        entry.delete(0,tk.END)

def delete_task():
    try:
        task_index = listbox.curselection()[0]
        listbox.delete(task_index)
    except IndexError:
        pass


root = tk.Tk()
root.title("To-Do-List APP")

icon_image = tk.PhotoImage(file="C:\\Users\\ARUN\\Desktop\\image\\icon.png")
root.tk.call('wm', 'iconphoto', root._w, icon_image)

new_width = 600
new_height = 600
root.geometry(f"{new_width}x{new_height}")


frame = tk.Frame(root, bg="white", width=new_width, height=new_height)
frame.place(relx=0.5, rely=0.5, anchor="center")

listbox = tk.Listbox(frame,selectbackground = "lightgray")
listbox.pack(pady=10)

entry = tk.Entry(frame,font = ("italic",16))
entry.pack(pady = 10)

add_button = tk.Button(frame,text = "ADD",command = add_task)
delete_button = tk.Button(frame,text = "DELETE",command = delete_task)
add_button.pack(pady = 10)
delete_button.pack(pady = 10)

root.mainloop()
           
