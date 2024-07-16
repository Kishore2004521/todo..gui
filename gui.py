import tkinter as tk

class TodoListApp:
    def _init_(self, master):
        self.master = master
        master.title("Todo List")
        self.entry_frame = tk.Frame(master)
        self.entry_frame.pack(fill=tk.X)
        self.todo_entry = tk.Entry(self.entry_frame)
        self.todo_entry.pack(side=tk.LEFT, expand=True, fill=tk.X)
        self.add_button = tk.Button(self.entry_frame, text="Add", command=self.add_todo)
        self.add_button.pack(side=tk.RIGHT)
        self.list_frame = tk.Frame(master)
        self.list_frame.pack(fill=tk.Y, expand=True)
        self.todo_list = tk.Listbox(self.list_frame, selectmode=tk.SINGLE)
        self.todo_list.pack(fill=tk.BOTH, expand=True)
        self.edit_button = tk.Button(self.list_frame, text="Edit", state=tk.DISABLED, command=self.edit_todo)
        self.edit_button.pack(side=tk.LEFT)
        self.delete_button = tk.Button(self.list_frame, text="Delete", state=tk.DISABLED, command=self.delete_todo)
        self.delete_button.pack(side=tk.LEFT)
        self.todos = []
        self.master.bind("<Return>", self.add_todo_key)
        self.master.bind("<F2>", self.edit_todo_key)
    def add_todo(self):
        todo = self.todo_entry.get().strip()
        if todo:
            self.todos.append(todo)
            self.todo_list.insert(tk.END, todo)
            self.todo_entry.delete(0, tk.END)
            self.update_buttons()
    def add_todo_key(self, event):
            self.add_todo()

    def edit_todo(self):
        selected_index = self.todo_list.curselection()
        if selected_index:
            index = selected_index[0]
            new_todo = self.todo_entry.get().strip()
            if new_todo:
                self.todos[index] = new_todo
                self.todo_list.delete(index)
                self.todo_list.insert(index, new_todo)
                self.todo_entry.delete(0, tk.END)
                self.update_buttons()

    def edit_todo_key(self, event):
        self.edit_todo()

    def delete_todo(self):
        selected_index = self.todo_list.curselection()
        if selected_index:
            index = selected_index[0]
            self.todos.pop(index)
            self.todo_list.delete(index)
            self.update_buttons()

    def update_buttons(self):
        selected_index = self.todo_list.curselection()
        self.edit_button.config(state=tk.NORMAL if selected_index else tk.DISABLED)
        self.delete_button.config(state=tk.NORMAL if selected_index else tk.DISABLED)


root = tk.Tk()
app = TodoListApp()


