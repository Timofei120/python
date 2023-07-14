import tkinter # графическое окно
from PIL import ImageTk, Image # картинки
import os # работа с файлами

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # путь к папке проекта


def like():
    """обработка нажатия на кнопку лайк

    :return:
    """
    global total_like, like_label, current_image_index
    total_like += 1
    like_label.config(text=f'лайков: {total_like}')
    current_image_index = (current_image_index + 1) % len(images_filenames)
    uptade_image()


def dislike():
    '''обработка нажатие на кнопку дизлайк

    :return:
    '''
    global total_dislike, dislike_label, current_image_index
    total_dislike += 1
    dislike_label.config(text=f'дизлайков: {total_dislike}')
    current_image_index = (current_image_index + 1) % len(images_filenames)
    uptade_image()


def uptade_image():
    '''обнавление фото

    :return:
    '''
    image_path = os.path.join(image_derectory, images_filenames[current_image_index])
    image = Image.open(image_path)
    image = image.resize((300, 200), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)

    image_label.config(image=photo)
    image_label.image = photo


total_like = 0
total_dislike = 0
current_image_index = 0
image_derectory = os.path.join(BASE_DIR, 'images')
images_filenames = sorted(os.listdir(image_derectory))

root = tkinter.Tk()
root.title('лайк-дизлайк')
root.geometry('400x450')
root.resizable(False, False)

image_path = os.path.join(image_derectory, images_filenames[current_image_index])
image = Image.open(image_path)
image = image.resize((300, 200), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)

image_label = tkinter.Label(root, image=photo)
image_label.pack(pady=10)

like_image = Image.open('like.png')
dislike_image = Image.open('dislike.png')

like_image = like_image.resize((100, 100), Image.LANCZOS)
dislike_image = dislike_image.resize((100, 100), Image.LANCZOS)

like_image = ImageTk.PhotoImage(like_image)
dislike_image = ImageTk.PhotoImage(dislike_image)

buttons_frame = tkinter.Frame(root)
buttons_frame.pack(pady=20)

# кнопка лайк
like_button = tkinter.Button(buttons_frame, image=like_image, bd=0, command=like)
like_button.pack(side=tkinter.LEFT, padx=10)

dislike_button = tkinter.Button(buttons_frame, image=dislike_image, bd=0, command=dislike)
dislike_button.pack(side=tkinter.RIGHT, padx=10)

# контейнер для кол-ва лайков

like_label = tkinter.Label(root, text='лайков: 0', font=('Arial', 14))
like_label.pack()

dislike_label = tkinter.Label(root, text='дизлайков: 0', font=('Arial', 14))
dislike_label.pack()

root.mainloop()
