# -*- coding:utf-8 -*-
import tkinter
import tkinter.filedialog
import os
from PIL import ImageGrab
from time import sleep
from tkinter import StringVar, IntVar

#截图区域选择
class MyCapture:
    def __init__(self, root, png):
        # 变量X和Y用来记录鼠标左键按下的位置
        self.X = tkinter.IntVar(value=0)
        self.Y = tkinter.IntVar(value=0)

        self.selectPosition = None
        # 屏幕尺寸
        screenWidth = root.winfo_screenwidth()
        # print(screenWidth)
        screenHeight = root.winfo_screenheight()
        # print(screenHeight)
        # 创建顶级组件容器
        self.top = tkinter.Toplevel(root, width=screenWidth, height=screenHeight)
        # 不显示最大化、最小化按钮
        self.top.overrideredirect(True)
        self.canvas = tkinter.Canvas(self.top, bg='white', width=screenWidth, height=screenHeight)
        # 显示全屏截图，在全屏截图上进行区域截图
        self.image = tkinter.PhotoImage(file=png)
        self.canvas.create_image(screenWidth // 2, screenHeight // 2, image=self.image)

        # 鼠标左键按下的位置
        def onLeftButtonDown(event):
            self.X.set(event.x)
            self.Y.set(event.y)
            # 开始截图
            self.sel = True

        self.canvas.bind('<Button-1>', onLeftButtonDown)

        # 鼠标左键移动，显示选取的区域
        def onLeftButtonMove(event):
            if not self.sel:
                return
            global lastDraw
            try:
                # 删除刚画完的图形，要不然鼠标移动的时候是黑乎乎的一片矩形
                self.canvas.delete(lastDraw)
            except Exception as e:
                pass
            lastDraw = self.canvas.create_rectangle(self.X.get(), self.Y.get(), event.x, event.y, outline='black')

        self.canvas.bind('<B1-Motion>', onLeftButtonMove)

        # 获取鼠标左键抬起的位置，保存区域截图
        def onLeftButtonUp(event):
            self.sel = False
            try:
                self.canvas.delete(lastDraw)
            except Exception as e:
                pass
            sleep(0.1)
            # 考虑鼠标左键从右下方按下而从左上方抬起的截图
            myleft, myright = sorted([self.X.get(), event.x])
            mytop, mybottom = sorted([self.Y.get(), event.y])
            self.selectPosition = (myleft, myright, mytop, mybottom)
            #             pic = ImageGrab.grab((left+1, top+1, right, bottom))
            #
            #             #弹出保存截图对话框
            #
            #             fileName = tkinter.filedialog.asksaveasfilename(title='保存截图', filetypes=[('JPG files', '*.jpg')])
            #
            #             if fileName:
            #
            #                 pic.save(fileName+'.jpg')
            # 关闭当前窗口
            # print(left, '  ', top,'  ',right,'  ',bottom)

            self.top.destroy()

        self.canvas.bind('<ButtonRelease-1>', onLeftButtonUp)
        self.canvas.pack(fill=tkinter.BOTH, expand=tkinter.YES)
        # 开始截图

    def pos_get(self):
        return self.selectPosition

