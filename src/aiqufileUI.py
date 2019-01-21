from tkinter import *
from tkinter.filedialog import askdirectory as askDir
import time
from os.path import join as pathJoin
from aiquTk import *

import scanner


def selectPath(rootPath):
    thePath = askDir()
    rootPath.set(thePath)
    print(rootPath.get())


def textClear(textList):
    for x in textList:
        x.config(state=NORMAL)
        x.delete(1.0, END)
        x.config(state=DISABLED)


def findDupFile(fileList):
    print("findDupFile")

def fileFind(name, rootpath, flag):
    print("fileFinding")


def mkTimerGroup(master):
    timeVal = StringVar()
    timerLabel = mkLable(master, " ", row=0, column=8, sticky=Right, val=timeVal)

    def updateTime():
        nonlocal timeVal
        nonlocal timerLabel
        timeVal.set(time.strftime("%Y-%m-%d %H:%M:%S   %A", time.localtime()))
        timerLabel.after(1000, updateTime)

    updateTime()


def mkComGroup(master, outFrame):
    mkLable(master, "文件路径", row=0, column=0)
    mkLable(master, "公共选项", row=2, column=0)

    var1 = IntVar()
    mkCkButton(master, "递归子目录", var=var1, row=3, column=1, isSelect=True)

    rootpath = StringVar()
    pathEntry = mkEntry(master, var=rootpath, size=50, row=0, column=1, columnspan=3)

    mkButton(master, "选择目录", 0, 4, selectPath, rootpath)
    outText = mkScrollText(outFrame, width=40, height=31, row=0, column=0, columnspan=1)
    return {'recursion': var1, 'path': pathEntry, 'out': outText}


'''      
def scanDup(rootPath, options):
    fileList = fileScan.dirScan(rootPath, options['recursion'])
    dupFileList = findDupFile(fileList[1])

    return dupFileList
'''


def textPrint(dupText, dataList, thisLabel=None, clear=True):
    # dupText = mkScrollText(master, width=40, height=31, row=0, column=0, columnspan=1)
    dupText.config(state=NORMAL)
    if clear: dupText.delete(1.0, END)
    for x in dataList: dupText.insert(END, x + '\n')
    dupText.config(state=DISABLED)


def dupProc(master, params):
    print(dupProc)

def mkDupGroup(master, this, common):
    mkLable(this, "选项", row=0, column=0)
    var2 = IntVar()
    var3 = IntVar()
    mkCkButton(this, "文件名匹配", var=var2, row=0, column=1, isSelect=True)
    mkCkButton(this, "MD5值匹配", var=var3, row=0, column=2, isSelect=False)
    mkButton(this, "扫描重复文件", 1, 5, dupProc, master, {'common': common, 'matchN': var2, 'matchM': var3})

    return


def findProc(master, params):
    common = params['common']
    fileName = params['file'].get()
    rootPath = common['path'].get()
    option = params['match'].get()
    findText = common['out']
    # findText = mkScrollText(master, width=40, height=31, row=0, column=0, columnspan=1)

    if rootPath and fileName:
        findList = fileFind(fileName, rootPath, option)
        textPrint(findText, findList)
    else:
        print('please in put a file name and path')


def mkFindGroup(master, this, common):
    mkLable(this, "文件名", row=0, column=0)
    mkLable(this, "选项", row=1, column=0)
    var4 = IntVar()
    mkCkButton(this, "文件名精确匹配", var4, row=1, column=1, isSelect=False)

    fileName = StringVar()
    fileEntry = mkEntry(this, fileName, size=50, row=0, column=1, columnspan=3)

    params = {'common': common, 'file': fileEntry, 'match': var4}
    mkButton(this, "查找", 2, 4, findProc, master, params)
    return


def mkImageGroup(this, img):
    # img = PhotoImage(file='img.gif')
    imgLabel = Label(this, image=img)
    imgLabel.grid(row=0, column=0)
    return imgLabel


def mkwindow(title, width, height):
    master = mkTk(title, width, height)

    commFrame = mkFrame(master, width=600, height=120, row=0, column=0)
    dupFrame = mkFrame(master, width=600, height=120, row=1, column=0)
    findFrame = mkFrame(master, width=600, height=120, row=2, column=0)
    clockFrame = mkFrame(master, width=300, height=100, row=0, column=1, rowspan=1, bg='SkyBlue')
    outFrame = mkFrame(master, width=300, height=400, row=1, column=1, rowspan=4)

    imageFrame = mkFrame(master, width=600, height=100, row=3, column=0)

    clockFrame.grid_propagate(0)
    outFrame.grid_propagate(0)

    mkTimerGroup(clockFrame)
    common = mkComGroup(commFrame, outFrame)
    dupGroup = mkDupGroup(outFrame, dupFrame, common)
    findGroup = mkFindGroup(outFrame, findFrame, common)

    #img = PhotoImage(file='img.gif')
    #imgGroup = mkImageGroup(imageFrame, img)

    master.mainloop()


if __name__ == '__main__':
    mkwindow('我的工具', 900, 500)
