import tkinter as tk
from tkinter import *

from PIL import ImageTk, Image
from tkinter import messagebox


root = Tk()
root.title("predicting_platform")
root.geometry('5000x5000')

#로고
my_img1 = Image.open('/Users/b/Desktop/logo.png')
resize_image1 = my_img1.resize((200, 150))
img1 = ImageTk.PhotoImage(resize_image1)

label_logo = tk.Label(root,image=img1)
label_logo.pack()

#예시 표
my_img2 = Image.open('/Users/b/Desktop/example.png')
resize_image2 = my_img2.resize((400, 150))
img2 = ImageTk.PhotoImage(resize_image2)

label_example = tk.Label(root,image=img2)
label_example.pack()


#문구
label_entry = tk.Label(root, text='위에 나와있는 데이터를 바탕으로 승리자를 예측해보세요!', font=('Arial', 15))
label_entry.pack()

#pandas로 데이터 시각화할 거라면, 
#사람들이 예측하는 바탕이 될 수 있는 데이터를 시각화한 pandas 표가 
#이 label_entry 위에 뜰 수 있게 코딩하면 될 것 같음.

#사람들이 예측하는 값이 입력되는 곳 = Entry
myentry= tk.Entry(root)
myentry.pack()

#예측값을 돌려주는 함수
def get_prediction():
    if myentry.get() == None:
        return None
    else:
        prediction = myentry.get()
        print(prediction)
    #print(self.check_state.get()) gives us the state of the checkbox. nonchecked -> 0, checked -> 1
        return prediction

#예측값을 '최종 제출'하는 버튼
button = tk.Button(root, text='done', font=('arial', 13), command=get_prediction, relief = 'groove')
button.pack(ipadx=5, ipady=5, expand=True)
#참고로 이 버튼 배경색... 남색인데 macOS는 bug 때문에 이게 하얀색으로 나타난다고 함.;;

#창 닫을 때, 닫히기 전 경고문 뜨게 하는 구문
def closing():
    if messagebox.askyesno(title='Quit?', message = 'Do you really want to quit?'):
        root.destroy()

root.protocol('WM_DELETE_WINDOW', closing)


#메뉴바
menubar = tk.Menu(root)
changemenu = tk.Menu(menubar, tearoff = 0)
changemenu.add_command(label = '다른 자료로 예측')
#여기에 filemenu.add_command(label = '다른 자료로 예측', command=????)
#????에 다른 데이터자료, 즉 다른 판다스 표가 나오게 하면 될 것 같음.

#기여한 사람 목록 
def show_people():
    messagebox.showinfo(title='people', message='이서준, 김민서, 전하성, 권예람, 이상수')

#동아리 설명
def show_info():
    messagebox.showinfo(title='club', message='소프트웨어와 하드웨어 프로젝트를 동료들과 함께 다루는 공학 연합 동아리')

    
aboutmenu= tk.Menu(menubar, tearoff = 0)
aboutmenu.add_command(label='contributers', command = show_people)
aboutmenu.add_command(label='what is DECFI', command = show_info)


menubar.add_cascade(menu=changemenu, label = 'Prediction')
menubar.add_cascade(menu=aboutmenu, label = 'About')

    
root.config(menu=menubar)

root.mainloop()
