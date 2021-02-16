from datetime import datetime
import tkinter
import time

w=150
h=150

root1=tkinter.Tk()
root1.title("timer")
root1.geometry("150x100")
root1.attributes("-topmost", True)
canvas=tkinter.Canvas(root1,width=w,heigh=h)
canvas.pack()#ここを書かないとcanvasがうまく入らない．

while True:
    now_h=datetime.now().hour
    now_s=datetime.now().second
    now_m=datetime.now().minute
    now_time=str(now_h)+":"+str(now_m)+":"+str(now_s)
    canvas.create_text(w/2,40,text=now_time,font=("",20,"italic"),tag='Y') #タグを入れることで更新できるようにする．
    canvas.update()
    canvas.delete('Y')
    time.sleep(0.5)


