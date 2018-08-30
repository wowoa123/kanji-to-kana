import sys
import tkinter


def text(master, sentence):
    master.geometry('1000x150+400+50')
    master.overrideredirect(False)
    master.attributes('-topmost', True,
                      '-alpha', 0.5,
                      '-toolwindow', True)
    label = tkinter.Label(master, text=sentence, font=("Arial", 25))
    label.pack()


if __name__ == '__main__':
    root = tkinter.Tk()
    text(root, sys.argv[1])
    root.mainloop()