import random
import tkinter
from tkinter import messagebox
from PIL import Image, ImageTk

def generate_secret_number():
    return random.randint(1, 100)


def check_gues(secret_number, guess):
    '''

    :param secret_number: загаданное число
    :param guess: введённое число
    :return: результат
    '''
    global guesses_taken
    if guess < secret_number:
        guesses_taken += 1
        return 'холодно'
    elif guess > secret_number:
        guesses_taken += 1
        return 'горячо'
    else:
        return 'Победа'


def check_button():
    guess = int(entry.get())
    result = check_gues(secret_number=secret_number, guess=guess)
    result_label.config(text=result)

    if result == 'Победа':
        message = f'вы угадали число за {guesses_taken} попыток!'
        messagebox.showinfo(title='победа!', message=message)
        root.destroy()

root = tkinter.Tk()
root.title('холодно-горячо')

backgraund_image = Image.open('3d-render-realistic-chess-isolated-pastel-purple-background-illustration-design.jpg')

window_width, window_height = 800, 600
backgraund_image = backgraund_image.resize((window_width,window_height), Image.LANCZOS)
backgraund_photo = ImageTk.PhotoImage(backgraund_image)
backgraund_label = tkinter.Label(root, image=backgraund_photo)
backgraund_label.place(x=0, y=0, relwidth=1, relheight=1)

root.geometry(f'{window_width}x{window_height}')
root.resizable(False, False)

instraction_label = tkinter.Label(root, text='я загадал число от 1 до 100. попробуй угадай',
                                  font=('Arial', 18), bg='white')
instraction_label.place(relx=0.5, rely=0.2, anchor='center')

entry = tkinter.Entry(root, font=('Arial', 15))
entry.place(relx=0.5, rely=0.5, anchor='center')

check_button = tkinter.Button(root, text='проверить', font=('Arial', 15),
                              bg='#4CAF50', fg='white', activebackground='#4CAF50',
                              activeforeground='white', command=check_button)
# def play_game():
#     '''
#
#     :return:
#     '''
#
#     secret_number = generate_secret_number()
#     guesses_taken = 0
#
#     print('я загадал число от 1 до 100.Попробуй отгадать его')
#
#     while True:
#         guess = int(input('введите ваше число'))
#         guesses_taken += 1
#
#         result = check_gues(secret_number=secret_number, guess=guess)
#         print(result)
#
#         if result == 'победа':
#             print(f'вы угадали число за {guesses_taken} попыток')
#             break
#
#
# if __name__ == '__main__':
#     play_game()

check_button.place(relx=0.5, rely=0.6, anchor='center')

result_label = tkinter.Label(root, font=('Arial', 15), fg='black', bg='white')
result_label.place(relx=0.5, rely=0.7, anchor='center')

secret_number = generate_secret_number()
guesses_taken = 0

root.mainloop()

