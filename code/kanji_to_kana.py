# -*- coding:utf-8 -*-

import configparser
import subprocess
import tkinter.messagebox
from multiprocessing import Process

from pynput import keyboard
from pynput.keyboard import Listener

import mecab
from area_select import *

# 创建tkinter主窗口
root = tkinter.Tk()
# 指定主窗口位置与大小
root.geometry('300x100+400+300')
# 不允许改变窗口大小
root.resizable(False, False)
# 窗口标题
root.title("kanji to kana")
# 窗口图标
root.iconbitmap('favicon.ico')
root.attributes('-topmost', True)

exist_p = False
p_pos = None

config_name = 'config.ini'


def config_save(option, value):
    cf = configparser.ConfigParser()
    cf.read(config_name)
    cf.set('config', option, value)
    with open(config_name, 'r+') as f:
        cf.write(f)


def config_get(option):
    cf = configparser.ConfigParser()
    cf.read(config_name)
    return cf.get("config", option)


def show_text(sentence):
    text = tkinter.Tk()
    text.overrideredirect(True)
    text.geometry('1000x150+400+50')
    w = tkinter.Label(text, text=sentence)
    w.pack()


def on_any_press(key):
    if key in keyboard.Key:
        return True
    else:
        c = key.char
        if (' ' < c < 'A') or ('Z' < c < 'a') or ('z' < c < 127):
            return True
        elif 'a' <= c.lower() <= 'z':
            return True
    return False


def on_press1(key):
    if on_any_press(key):
        config_save('hotkey', str(key))
        return False


def on_press2(key):
    if on_any_press(key):
        config_save('stop', str(key))
        return False


def on_press(key):
    pass


def on_release(key):
    pass


def hotkey_release(key):
    c = str(key)
    hotkey = config_get('hotkey')
    stop = config_get('stop')
    area = config_get('area')
    area = area[1:-1]
    area = area.split(',')
    if c == hotkey:
        result = mecab.to_kana(int(area[0]), int(area[2]), int(area[1]), int(area[3]))
        global exist_p
        global p_pos
        if not exist_p:
            p = subprocess.Popen(['pythonw', 'text_area.py', result])
            p_pos = p
            exist_p = True
        else:
            p = subprocess.Popen(['pythonw', 'text_area.py', result])
            p_pos.terminate()
            p_pos = p
    elif c == stop:
        return False


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

    config_save('area', str(w.pos_get()))

    return True


def buttonHotKeyClick():
    # 监听
    with Listener(on_press=on_press1, on_release=on_release) as listener:
        listener.join()
    # 提示
    tkinter.messagebox.showinfo('', config_get('hotkey') + '键已被设为默认键')

    return True


def buttonHookOnClick():
    with Listener(on_press=on_press, on_release=hotkey_release) as listener:
        listener.join()


def buttonHookOffClick():
    with Listener(on_press=on_press2, on_release=on_release) as listener:
        listener.join()
    # 提示
    tkinter.messagebox.showinfo('', config_get('stop') + '键已被设为停止键')

    return True


if not os.path.exists(config_name):
    cf = configparser.ConfigParser()
    cf.add_section('config')
    cf.set("config", "area", " ")
    cf.set("config", "hotkey", " ")
    cf.set("config", "stop", " ")
    with open(config_name, 'w') as f:
        cf.write(f)

# 截图区域按钮
ButtonCapture = tkinter.Button(root, text='截图区域选择', command=buttonCaptureClick)
ButtonCapture.place(x=35, y=10, width=100, height=30)

# 截图快捷键设定按钮
ButtonHotKey = tkinter.Button(root, text='截图快捷键设定', command=buttonHotKeyClick)
ButtonHotKey.place(x=35, y=60, width=100, height=30)

# 监听开始按钮
ButtonHookOn = tkinter.Button(root, text='开始转换', command=buttonHookOnClick)
ButtonHookOn.place(x=175, y=10, width=100, height=30)

# 停止按钮
ButtonHookOff = tkinter.Button(root, text='停止快捷键设定', command=buttonHookOffClick)
ButtonHookOff.place(x=175, y=60, width=100, height=30)

root.mainloop()
