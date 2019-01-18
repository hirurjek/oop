from tkinter import *
from controllers.MainWindowController import Controller
#pip install pil
#pip install pyzbar

if __name__ == '__main__':
    root = Tk()
    root.title('QR - decoder')
    root.tk_setPalette(background='#FFFFFF')
    root.geometry("800x450+600+250")
    root.resizable(False, False)
    app = Controller(root)
    root.mainloop()
