import tkinter as tk
from tkinter import messagebox

class BMICalculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculadora de IMC")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Altura (M):").grid(row=0, column=0, padx=10, pady=9)
        tk.Label(self.root, text="Peso (Kg):").grid(row=1, column=0, padx=10, pady=9)
        
        self.height_entry = tk.Entry(self.root)
        self.weight_entry = tk.Entry(self.root)
        self.height_entry.grid(row=0, column=1, padx=10, pady=9)
        self.weight_entry.grid(row=1, column=1, padx=10, pady=9)
        
        calculate_button = tk.Button(self.root, text="Calcule seu IMC", command=self.calculate_bmi)
        calculate_button.grid(row=2, columnspan=2, pady=9)
        
        self.result_label = tk.Label(self.root, text="Seu IMC aparecerá aqui")
        self.result_label.grid(row=3, columnspan=2, pady=9)

    def calculate_bmi(self):
        try:
            height = float(self.height_entry.get())
            weight = float(self.weight_entry.get())
            bmi = weight / (height ** 2)
            self.result_label.config(text=f"Seu IMC é: {bmi:.2f}")
            self.show_bmi_category(bmi)
        except ValueError:
            messagebox.showerror("Erro de Entrada", "Por favor, insira valores conforme o ex: 1.87")

    def show_bmi_category(self, bmi):
        if bmi < 18.5:
            category = "Abaixo do peso"
        elif 18.5 <= bmi < 24.9:
            category = "Peso normal"
        elif 25 <= bmi < 29.9:
            category = "Sobrepeso"
        else:
            category = "Obesidade"
        self.result_label.config(text=f"Seu IMC é: {bmi:.2f}\nCategoria: {category}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = BMICalculator()
    app.run()
