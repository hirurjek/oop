from tkinter import *
import os

from PIL import Image, ImageTk


class MainWindow(Frame):
    #конструктор
    def __init__(self, root):
        super().__init__(root)
        self.pack()
        self.root = root
        self.create_widgets()


    # создаем кнопки и т.д
    def create_widgets(self):
        self.image_uploaded = Image.open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),  'src/default.png')).convert('RGB')
        self.img = ImageTk.PhotoImage(image = self.image_uploaded)
        self.image_label = Label(self, image = self.img)
        self.decode_button = Button(self, text = 'Расшифровать', width =15, height = 2, font = 'sans-serif 8')
        self.search_qr_button = Button(self, text = 'Найти QR - коды', width = 15, height =2, font = 'sans-serif 8')
        self.label_result = Label(self, height=3, text = "Расшифрованные коды: ", bg = '#fff', font = 'ff-kava 16')
        self.codes_list = Listbox(self, height = 15)
        self.image_label.pack(pady=10, side = LEFT)
        self.label_result.pack(padx = 25 , pady = 12, fill = X)
        self.codes_list.pack(padx = 25, fill = X)
        self.decode_button.pack(padx = 25, side = LEFT)
        self.search_qr_button.pack(padx = 25, side = RIGHT)


if __name__ == '__main__':
     root = Tk()
     root.geometry("800x650+400+10")
     root.resizable(False, False)
     root.title("QR - decoder")
     app = MainWindow(root)
     root.mainloop()
