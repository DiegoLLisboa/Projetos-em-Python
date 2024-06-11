import tkinter as tk
from tkinter import messagebox
import os
import pickle

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tarefas")

        self.tasks_file = "tasks.pkl"

        main_frame = tk.Frame(root)
        main_frame.pack(pady=10, padx=10)

        entry_frame = tk.Frame(main_frame)
        entry_frame.grid(row=0, column=0, columnspan=2, pady=5)

        self.label = tk.Label(entry_frame, text="Digite a tarefa:")
        self.label.pack(side=tk.LEFT)

        self.task_entry = tk.Entry(entry_frame, width=50)
        self.task_entry.pack(side=tk.LEFT, padx=5)
        self.task_entry.bind("<Return>", self.add_task)

        self.add_button = tk.Button(entry_frame, text="Adicionar Tarefa", command=self.add_task)
        self.add_button.pack(side=tk.LEFT)

        self.tasks_frame = tk.Frame(main_frame)
        self.tasks_frame.grid(row=1, column=0, pady=5)

        actions_frame = tk.Frame(main_frame)
        actions_frame.grid(row=1, column=1, padx=10, pady=5, sticky='n')

        self.remove_button = tk.Button(actions_frame, text="Remover Tarefa(s)", command=self.remove_task)
        self.remove_button.pack(pady=5)

        self.reset_button = tk.Button(actions_frame, text="Resetar Seleção", command=self.reset_selection)
        self.reset_button.pack(pady=5)

        self.tasks = []

        self.load_tasks()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def add_task(self, event=None):
        task_text = self.task_entry.get()
        if task_text:
            var = tk.BooleanVar()
            cb = tk.Checkbutton(self.tasks_frame, text=task_text, variable=var)
            cb.pack(anchor='w')
            self.tasks.append((cb, var))
            self.task_entry.delete(0, tk.END)
            self.save_tasks()
        else:
            messagebox.showwarning("Entrada inválida", "Por favor, digite uma tarefa.")

    def remove_task(self):
        for cb, var in self.tasks[:]:
            if var.get():
                cb.pack_forget()
                self.tasks.remove((cb, var))
        self.save_tasks()

    def reset_selection(self):
        for cb, var in self.tasks:
            var.set(False)

    def save_tasks(self):
        tasks_data = [(cb.cget('text'), var.get()) for cb, var in self.tasks]
        with open(self.tasks_file, 'wb') as file:
            pickle.dump(tasks_data, file)

    def load_tasks(self):
        if os.path.exists(self.tasks_file):
            with open(self.tasks_file, 'rb') as file:
                tasks_data = pickle.load(file)
                for task_text, task_state in tasks_data:
                    var = tk.BooleanVar(value=task_state)
                    cb = tk.Checkbutton(self.tasks_frame, text=task_text, variable=var)
                    cb.pack(anchor='w')
                    self.tasks.append((cb, var))

    def on_closing(self):
        self.save_tasks()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
