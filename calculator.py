import tkinter as tk
import math

class SmartCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Scientific Calculator")
        self.root.geometry("380x560")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e2e")

        self.expression = ""

        # Display Screen
        self.display = tk.Entry(
            root, 
            font=("Helvetica", 22, "bold"), 
            bg="#313244", 
            fg="#cdd6f4", 
            bd=0, 
            justify="right", 
            insertbackground="white"
        )
        self.display.pack(fill="both", ipadx=8, ipady=15, padx=15, pady=15)
        buttons = [
            ('C', 1, 0), ('(', 1, 1), (')', 1, 2), ('/', 1, 3),
            ('sin', 2, 0), ('cos', 2, 1), ('tan', 2, 2), ('*', 2, 3),
            ('√', 3, 0), ('^', 3, 1), ('log', 3, 2), ('-', 3, 3),
            ('7', 4, 0), ('8', 4, 1), ('9', 4, 2), ('+', 4, 3),
            ('4', 5, 0), ('5', 5, 1), ('6', 5, 2), ('%', 5, 3),
            ('1', 6, 0), ('2', 6, 1), ('3', 6, 2), ('=', 6, 3),
            ('0', 7, 0), ('.', 7, 1)
        ]

        # Container for buttons
        btn_frame = tk.Frame(root, bg="#1e1e2e")
        btn_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Configure grid expansion
        for i in range(8):
            btn_frame.rowconfigure(i, weight=1)
        for j in range(4):
            btn_frame.columnconfigure(j, weight=1)

        # Create Buttons
        for b in buttons:
            text, row, col = b[0], b[1], b[2]
            self.create_button(btn_frame, text, row, col)

    def create_button(self, parent, text, row, col):
        bg_color = "#45475a"
        fg_color = "#cdd6f4"

        if text in ['/', '*', '-', '+', '%']:
            bg_color = "#fab387"
            fg_color = "#11111b"
        elif text == '=':
            bg_color = "#a6e3a1"
            fg_color = "#11111b"
        elif text in ['C', '√', 'sin', 'cos', 'tan', 'log', '^', '(', ')']:
            bg_color = "#f38ba8"
            fg_color = "#11111b"

        btn = tk.Button(
            parent, 
            text=text, 
            font=("Helvetica", 13, "bold"),
            bg=bg_color, 
            fg=fg_color, 
            bd=0,
            activebackground="#b4befe",
            command=lambda: self.on_button_click(text)
        )
        if text == '0':
            btn.grid(row=row, column=col, columnspan=2, sticky="nsew", padx=3, pady=3)
        elif text == '.':
            btn.grid(row=row, column=col+1, sticky="nsew", padx=3, pady=3)
        else:
            btn.grid(row=row, column=col, sticky="nsew", padx=3, pady=3)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.update_display("")
        elif char == '=':
            self.calculate_result()
        elif char == '√':
            self.expression += "math.sqrt("
            self.update_display(self.expression)
        elif char == '^':
            self.expression += "**"
            self.update_display(self.expression)
        elif char in ['sin', 'cos', 'tan', 'log']:
            self.expression += f"math.{char}("
            self.update_display(self.expression)
        elif char == '%':
            self.expression += "/100"
            self.update_display(self.expression)
        else:
            self.expression += str(char)
            self.update_display(self.expression)

    def update_display(self, value):
        self.display.delete(0, tk.END)
        self.display.insert(0, value)

    def calculate_result(self):
        try:
            expr = self.expression
            open_brackets = expr.count('(')
            close_brackets = expr.count(')')
            if open_brackets > close_brackets:
                expr += ')' * (open_brackets - close_brackets )
            result = eval(expr, {"__builtins__": None, "math": math})
            
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            
            self.update_display(str(result))
            self.expression = str(result)
        except ZeroDivisionError:
            self.update_display("Cannot divide by zero")
            self.expression = ""
        except Exception:
            self.update_display("Error")
            self.expression = ""

if __name__ == "__main__":
    root = tk.Tk()
    app = SmartCalculator(root)
    root.mainloop()