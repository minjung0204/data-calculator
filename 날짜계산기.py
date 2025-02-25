from datetime import datetime, timedelta
from tkinter import *

root = Tk()
root.title("날짜계산기")
root.geometry("640x480")
#root.geometry("640x480+100+300") # 가로 * 세로 + x좌표 + y좌표

# root.resizable(False, False) # x(너비), y(높이) 값 변경 불가 (창 크기 변경 불가)

label1 = Label(root, text = "YYYY-MM-DD 형식으로 날짜를 입력하세요.\n (예: 2024-12-09) ")
label1.pack()

txt = Text(root, width=20, height=1)
txt.pack()





root.mainloop()