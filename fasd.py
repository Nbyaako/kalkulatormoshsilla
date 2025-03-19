import tkinter as tk
from tkinter import messagebox

def on_button_click(char):

  current = entry.get()
  if char == '=':
    try:
      result = eval(current)
      entry.delete(0, tk.END)
      entry.insert(0, str(result))
    except (SyntaxError, ZeroDivisionError):
      messagebox.showerror("Ошибка", "Прогремел офигительный бумбокс")
  elif char == 'C':
    entry.delete(0, tk.END)
  else:
    entry.insert(tk.END, char)


window = tk.Tk()
window.title("калькулятор")

entry = tk.Entry(window, width=20, font=('ansifixed', 10), justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=7, pady=1)


button_color = "#ADD8E6"
special_button_color = "#90EE90"
text_color = "black"

buttons = [
  ('7', '8', '9', '/'),
  ('4', '5', '6', '*'),
  ('1', '2', '3', '-'),
  ('0', '.', '=', '+'),
  ('C',)
]

row_num = 1
for row in buttons:
  col_num = 0
  for char in row:
    if char == 'C' or char in ['=', '/', '*', '-', '+']:
      button = tk.Button(window, text=char, padx=10, pady=10, font=('ansifixed', 20),
                           command=lambda c=char: on_button_click(c),
                           bg=special_button_color, fg=text_color)
      if char == 'C':
          button.grid(row=row_num, column=col_num, columnspan=10, padx=10, pady=10)
          break
      else:
          button.grid(row=row_num, column=col_num, padx=10, pady=10)

    else:
      button = tk.Button(window, text=char, padx=1, pady=1, font=('ansifixed', 17),
                           command=lambda c=char: on_button_click(c),
                           bg=button_color, fg=text_color)
      button.grid(row=row_num, column=col_num, padx=5, pady=5)
    col_num += 1
  row_num += 1



window.mainloop()