from models.Decoder import Decoder
from views.MainView import MainWindow
from PIL import ImageTk, Image
from tkinter import filedialog, END, messagebox


class Controller:

    def __init__(self, root):
        self.model = Decoder()
        self.view = MainWindow(root)

        # устанавливаем обработчики событий на нажатия кнопок
        self.view.decode_button.config(command = self.decode_qr)
        self.view.search_qr_button.config(command = self.search_qr)

    def decode_qr(self):

        image_file = filedialog.askopenfilename(initialdir = '/', title = "Select file", filetypes = (("all files", "*.*"),("jpeg files", "*.jpg"), ("png files", "*.png"), ("gif files", "*.gif"), ("bmp files", "*.bmp")))

        if image_file != '':

            try:
                image = Image.open(image_file).convert('RGB')

                if image.width != 400 and image.height != 400:
                    image = image.resize((400, 400))

                output_image = ImageTk.PhotoImage(image)

                self.view.img = output_image
                self.view.image_uploaded = image
                self.view.image_label.config(image = output_image)

                decoded_list = self.model.decodeImage(image)
                self.view.codes_list.delete(0, END)

                if len(decoded_list) == 0:
                    self.view.codes_list.insert(0, "QR  коды не найдены!")
                else:
                    for qr_data in decoded_list:
                        string_data = qr_data.data.decode('utf-8')
                        self.view.codes_list.insert(0, string_data)
            except OSError:
                messagebox.showerror('Ошибка', 'Невозможно открыть файл')



    def search_qr(self):

        output_image = ImageTk.PhotoImage(self.model.search_qr_code(self.view.image_uploaded))
        self.view.img = output_image
        self.view.image_label.config(image = output_image)




