# -*- coding:utf-8 -*-

import tkinter.messagebox
from tkinter import *
import win32api
import image_analy
import mecab
from gui_button import *
import screenshot
from pynput.keyboard import Listener
import logging

# 创建tkinter主窗口
root = tkinter.Tk()
# 指定主窗口位置与大小
root.geometry('300x100+400+300')
# 不允许改变窗口大小
root.resizable(False, False)
#窗口标题
root.title("kanji to kana")
#窗口图标
root.iconbitmap('favicon.ico')

config_name = 'config.cfg'
if not os.path.exists(config_name):
    with open(config_name, 'w') as f:
        f.write('area:                     hotkey:  stop:  ')
        f.seek(0, 0)

def buttonCaptureClick():
    # 最小化主窗口
    # root.state('icon')
    # sleep(0.2)

    filename = 'temp.png'
    im = ImageGrab.grab()
    im.save(filename)
    im.close()
    # 显示全屏幕截图
    w = MyCapture(root, filename)
    ButtonCapture.wait_window(w.top)

    # print(w.myleft,w.mybottom)
    # 截图结束，恢复主窗口，并删除临时的全屏幕截图文件
    # label.config(text='Hello')
    root.state('normal')
    os.remove(filename)

    with open(config_name, 'r+') as f:
        index = f.read().find('area')
        f.seek(index)
        f.write('area:' + str(w.pos_get()))
        f.seek(0, 0)

    return True

def buttonHotKeyClick():
    pass

    return True


def buttonHookOnClick():
    pass

def buttonHookOffClick():
    pass

    return True

#截图区域按钮
ButtonCapture = tkinter.Button(root, text='截图区域选择', command=buttonCaptureClick)
ButtonCapture.place(x=35, y=10, width=100, height=30)

#截图快捷键设定按钮
ButtonHotKey = tkinter.Button(root, text='截图快捷键设定', command=buttonHotKeyClick)
ButtonHotKey.place(x=35, y=60, width=100, height=30)

#监听开始按钮
ButtonHookOn = tkinter.Button(root, text='开始转换', command=buttonHookOnClick)
ButtonHookOn.place(x=175, y=10, width=100, height=30)

#停止按钮
ButtonHookOff = tkinter.Button(root, text='停止快捷键设定', command=buttonHookOffClick)
ButtonHookOff.place(x=175, y=60, width=100, height=30)


root.mainloop()