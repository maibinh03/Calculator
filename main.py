from tkinter import Tk
from gui import setup_gui

def main():
    me = Tk()
    me.geometry("354x460")
    me.title("Chương trình máy tính")
    me.config(background='Dark gray')

    setup_gui(me)

    me.mainloop()

if __name__ == "__main__":
    main()
