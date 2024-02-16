import random
import pyautogui as pgui
import win32con as con
import win32gui as gui

handle = gui.FindWindow(0,'qq')
def smaller():
    for i in range(500,0,-1):
        gui.MoveWindow(handle,300,300,i,i,con.SWP_SHOWWINDOW)

def bigger():
    for i in range(0,500,1):
        gui.MoveWindow(handle,300,300,i,i,con.SWP_SHOWWINDOW)

def flash():
    while 1 :
        gui.ShowWindow(handle,con.SW_HIDE)  # 隐藏
        gui.ShowWindow(handle, con.SW_SHOW)   # 出现

def move():
    while 1:
        left,top,right,bottom = gui.GetWindowRect(handle)
        mouse = pgui.position()
        x = random.randint(0,1800)
        y = random.randint(0,1000)

        if left < mouse.x <right:
            gui.MoveWindow(handle,x,y,500,500,con.SWP_SHOWWINDOW)

fan_selct = {
    1: smaller,
    2: bigger,
    3: flash,
    4: move,
}

def main():
    select = int(input('请输入功能代号:\n1.窗口变小\n2.窗口变大\n3.窗口闪缩\n4.窗口走位\n5.退出\n'))
    if select == 5:
        exit()
    if select == '':
        pass
    if select in fan_selct:
        try:
            fan_selct[select]()
        except:
            print('--------未打开qq----------')
        main()
    else:
        print('没有此功能')

if __name__=='__main__':

        main()