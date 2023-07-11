import tkinter
from PIL import ImageTk, Image


def calculate():
    try:
        height = float(height_entry.get())
        weight = float(weight_entry.get())

        result = weight / (height ** 2)

        result_label.config(text=f'индекс массы тела {result:.2f}')
    except ValueError:
        result_label.config(text="данные должны иметь числовой тип")

backgraund_image = Image.open('blue-office-stationery-with-copy-space.jpg')

window_width = 800
window_height = 600

root = tkinter.Tk()  # иницализация окна
root.title('калькулятор веса')  # название

backgraund_image = backgraund_image.resize((window_width,window_height), Image.LANCZOS)
backgraund_photo = ImageTk.PhotoImage(backgraund_image)
backgraund_label = tkinter.Label(root, image=backgraund_photo)
backgraund_label.place(x=0, y=0, relwidth=1, relheight=1)
root.geometry(f'{window_width}x{window_height}')

root.resizable(False,False)

# поле для ввода роста
height_label = tkinter.Label(root, text='рост (м):', font=('Arial', 14), fg='black')
height_label.place(relx=0.5, rely=0.4, anchor='center')  # размещение подсказки для ввода

height_entry = tkinter.Entry(root, font=('Arial', 14))
height_entry.place(relx=0.5, rely=0.45, anchor='center')

weight_label = tkinter.Label(root, text='вес (кг)', font=('Arial', 14), fg='black', bg='white')
weight_label.place(relx=0.5, rely=0.5, anchor='center')

weight_entry = tkinter.Entry(root, font=('Arial', 14))
weight_entry.place(relx=0.5, rely=0.55, anchor='center')

button = tkinter.Button(root, text='расчитать', font=('Arial', 14), command=calculate,
                        bg='#4CAF50', fg='white', activebackground='#45A049', activeforeground='white')
button.place(relx=0.5, rely=0.6, anchor='center')

result_label = tkinter.Label(root, font=('Arial', 14), bg='white', fg='black')
result_label.place(relx=0.5, rely=0.7, anchor='center')

root.mainloop()
