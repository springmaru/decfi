import tkinter as tk
from tkinter import *
import tkinter.ttk

from PIL import ImageTk, Image
from tkinter import messagebox
from tkmacosx import Button
from random import *

root = Tk()
root.title("predicting_platform")
root.geometry('1000x600')

#로고
my_img1 = Image.open('/Users/b/Desktop/logo.png')
resize_image1 = my_img1.resize((200, 150))
img1 = ImageTk.PhotoImage(resize_image1)

label_logo = tk.Label(root,image=img1)
label_logo.pack()

label_qstn = tk.Label(root, text='알고리즘보다 더 정확하게 경기 결과를 예측할 수 있을까?', font=('Arial', 20), fg='#000033')
label_qstn.pack()

#표 시각화

# 표 생성하기. columns는 컬럼 이름, display columns는 실행될 때 보여지는 순서다.
viewer_df=tkinter.ttk.Treeview(root, columns=["index", "first_country", 'second_country'], displaycolumns=["index", "first_country", 'second_country'], height =4)
viewer_df.pack(padx=20, pady=20)

# 각 컬럼 설정. 컬럼 이름, 컬럼 넓이, 정렬 등
viewer_df.column("index", width=100, anchor='center')
viewer_df.heading("index", text=" ", anchor='center')

viewer_df.column("first_country", width=100, anchor="center")
viewer_df.heading("first_country", text='Brazil', anchor="center")
#text=str(random_country_1)

viewer_df.column("second_country", width=100, anchor="center")
viewer_df.heading("second_country", text='South Korea', anchor="center")
#text=str(random_country_2)

viewer_df['show'] = 'headings'

# 표에 삽입될 데이터
datavalue_dict=[('득점과 득실 차이', 2, 2), ('승부차기 승률', '30%','65%'), ('경기당 평균 득점', 2.8, 1.4), ('경기 당 평균 실점', 0.3, 1.2)]

# 표에 데이터 삽입
for i in range(len(datavalue_dict)):
    viewer_df.insert('', 'end', text=i, values=datavalue_dict[i], iid=str(i)+"번")


#문구1
label_entry = tk.Label(root, text='위에 나와있는 데이터를 바탕으로 승리자를 예측해보세요!', font=('Arial', 15), fg='#000033')
label_entry.pack()

#문구2
label_entry2 = tk.Label(root, text='(나라 이름은 영어로, 첫 철자는 대문자로 적어야 오류가 안 나요!)', font=('Arial', 10), fg='#000033')
label_entry2.pack()

#pandas로 데이터 시각화할 거라면, 
#사람들이 예측하는 바탕이 될 수 있는 데이터를 시각화한 pandas 표가 
#이 label_entry 위에 뜰 수 있게 코딩하면 될 것 같음.

#enter 버튼을 누르면, done을 누른 것이나 마찬가지의 효과. get()함수가 그대로 작용된다. 
def shortcut(event):
   if event.state == 0 and event.keysym == 'Return':
        get_prediction()

#잘못된 이름을 입력할 경우 경고문이 뜨게 하고, get()로 가는 아이도 없게. 
def done_error():
    return messagebox.showinfo(message = '무언가 잘못 입력하신 것 같아요!')
    

#사람들이 예측하는 값이 입력되는 곳 = Entry
myentry= tk.Entry(root)
myentry.bind('<KeyPress>', shortcut)
myentry.pack(pady=15, padx=15)

country_list = ['Spain', 'Germany', 'Brazil', 'Portugal', 'Argentina', 'Switzerland', 'Uruguay', 'Colombia', 'Italy', 'England', 'Belgium', 'Greece', 'United States', 'Chile', 'Netherlands', 'Ukraine', 'France', 'Croatia', 'Russia', 'Mexico', 'Bosnia and Herzegovina', 'Algeria', 'Denmark', "Côte d'Ivoire", 'Slovenia', 'Ecuador', 'Scotland', 'Costa Rica', 'Romania', 'Serbia', 'Panama', 'Sweden', 'Honduras', 'Czech Republic', 'Turkey', 'Egypt', 'Ghana', 'Armenia', 'Cape Verde Islands', 'Venezuela', 'Wales', 'Austria', 'IR Iran', 'Nigeria', 'Peru', 'Japan', 'Hungary', 'Tunisia', 'Slovakia', 'Paraguay', 'Brazil', 'Spain', 'Portugal', 'Netherlands', 'Italy', 'Germany', 'Argentina', 'England', 'France', 'Croatia', 'Russia', 'Egypt', 'Greece', 'United States', 'Serbia', 'Uruguay', 'Mexico', 'Chile', 'Cameroon', 'Australia', 'Nigeria', 'Norway', 'Ukraine', 'Switzerland', 'Slovenia', 'Israel', "Côte d'Ivoire", 'Romania', 'Turkey', 'Algeria', 'Paraguay', 'Ghana', 'Czech Republic', 'Slovakia', 'Colombia', 'Denmark', 'Sweden', 'Honduras', 'Bulgaria', 'Costa Rica', 'Republic of Ireland', 'Gabon', 'Scotland', 'Ecuador', 'Japan', 'Latvia', 'Korea Republic', 'Burkina Faso', 'Venezuela', 'Lithuania', 'Brazil', 'Czech Republic', 'Netherlands', 'Mexico', 'United States', 'Spain', 'Portugal', 'France', 'Argentina', 'England', 'Nigeria', 'Denmark', 'Italy', 'Turkey', 'Cameroon', 'Sweden', 'Egypt', 'Japan', 'Germany', 'Greece', 'Tunisia', 'Uruguay', 'IR Iran', 'Croatia', 'Romania', 'Costa Rica', 'Colombia', 'Senegal', 'Poland', 'Korea Republic', 'Republic of Ireland', "Côte d'Ivoire", 'Paraguay', 'Saudi Arabia', 'Switzerland', 'Morocco', 'Russia', 'Bulgaria', 'Ecuador', 'Norway', 'Slovakia', 'Honduras', 'Australia', 'Serbia and Montenegro', 'Ukraine', 'Jamaica', 'Trinidad and Tobago', 'Ghana', 'Finland', 'Israel', 'France', 'Brazil', 'Argentina', 'Colombia', 'Portugal', 'Italy', 'Mexico', 'Spain', 'Netherlands', 'Yugoslavia', 'Germany', 'England', 'United States', 'Romania', 'Republic of Ireland', 'Czech Republic', 'Cameroon', 'Paraguay', 'Sweden', 'Denmark', 'Croatia', 'Turkey', 'Belgium', 'Uruguay', 'Slovenia', 'Honduras', 'Nigeria', 'Russia', 'Costa Rica', 'IR Iran', 'Tunisia', 'Japan', 'Norway', 'Saudi Arabia', 'Trinidad and Tobago', 'Ecuador', 'South Africa', 'Poland', 'Morocco', 'Korea Republic', 'Finland', 'Senegal', 'Egypt', 'Ukraine', 'Chile', "Côte d'Ivoire", 'Peru', 'Australia', 'Slovakia', 'China PR', 'Brazil', 'Germany', 'Czech Republic', 'Mexico', 'England', 'Argentina', 'Norway', 'Yugoslavia', 'Chile', 'Colombia', 'United States', 'Japan', 'Morocco', 'Italy', 'Spain', 'Russia', 'Egypt', 'France', 'Croatia', 'Korea Republic', 'Tunisia', 'Romania', 'Zambia', 'South Africa', 'Netherlands', 'Ecuador', 'Denmark', 'Sweden', 'Paraguay', 'Jamaica', 'Austria', 'Australia', 'Bolivia', 'Saudi Arabia', 'Bulgaria', 'Belgium', 'Peru', 'Uruguay', 'Portugal', 'Slovakia', 'Scotland', 'IR Iran', 'Kuwait', "Côte d'Ivoire", 'Lithuania', 'Republic of Ireland', 'Israel', 'Trinidad and Tobago', 'Cameroon', 'Thailand', 'China PR', 'Georgia', 'Turkey', 'Poland', 'Greece', 'Angola', 'Algeria', 'Costa Rica', 'United Arab Emirates', 'Guinea', 'Finland', 'Hungary', 'Zaire', 'Ukraine', 'Ghana', 'Mali', 'Burkina Faso', 'El Salvador', 'Mozambique', 'Quatar', 'FYR Macedonia', 'Iceland', 'Togo', 'Nigeria', 'Guatemala', 'Germany', 'Netherlands', 'Brazil', 'Italy', 'Spain', 'Norway', 'Romania', 'Argentina', 'Denmark', 'Sweden', 'Nigeria', 'Switzerland', 'France', 'Republic of Ireland', 'England', 'Mexico', 'Colombia', 'Uruguay', 'Russia', 'Zambia', "Côte d'Ivoire", 'Portugal', 'United States', 'Cameroon', 'Egypt', 'Ghana', 'Belgium', 'Morocco', 'Bulgaria', 'Tunisia', 'Greece', 'Poland', 'Scotland', 'Saudi Arabia', 'Wales', 'Austria', 'Korea Republic', 'Iceland', 'Ecuador', 'Chile', 'Northern Ireland', 'Zimbabwe', 'Bolivia', 'Slovakia', 'Czech Republic', 'Finland', 'Australia', 'Algeria', 'Mali', 'Honduras']

#예측값을 돌려주는 함수
def get_prediction():
    if myentry.get() in country_list:
        prediction = myentry.get()
        print(prediction)
    else:
        done_error()
        
    #print(self.check_state.get()) gives us the state of the checkbox. nonchecked -> 0, checked -> 1
        return prediction

#def change_df():
    


#예측값을 '최종 제출'하는 버튼
done_button = Button(root, text='done', font=('arial', 13), command=get_prediction, relief = 'groove', bg='#000033', fg='white', bordercolor = '#000033', borderless=1, activebackground='#2a2a5f')
done_button.pack(ipadx=5, ipady=5, expand=False)

change_button = Button(root, text='다른 경기 예측하기',font=('arial', 13), relief = 'groove', bg='#2a2a5f', fg='white', bordercolor = '#2a2a5f', borderless=1, activebackground='#49497c')
change_button.pack(ipadx=5, ipady=5, expand=False, padx=30, pady=30)
#command=change_df

#창 닫을 때, 닫히기 전 경고문 뜨게 하는 구문
def closing():
    if messagebox.askyesno(title='Quit?', message = 'Do you really want to quit?'):
        root.destroy()

root.protocol('WM_DELETE_WINDOW', closing)




#메뉴바
menubar = tk.Menu(root)

#기여한 사람 목록 
def show_people():
    messagebox.showinfo(title='people', message='이서준, 김민서, 전하성, 권예람, 이상수')

#동아리 설명
def show_info():
    messagebox.showinfo(title='club', message='소프트웨어와 하드웨어 프로젝트를 동료들과 함께 다루는 공학 연합 동아리')

    
aboutmenu= tk.Menu(menubar, tearoff = 0)
aboutmenu.add_command(label='contributers', command = show_people)
aboutmenu.add_command(label='what is DECFI', command = show_info)

menubar.add_cascade(menu=aboutmenu, label = 'About')

    
root.config(menu=menubar)



root.mainloop()
