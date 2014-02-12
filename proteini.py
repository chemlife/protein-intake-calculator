from time import sleep
from tkinter import *


def D(weight):
    x = 1.76
    y = 2.2
    res1 = int(x*weight)
    res2 = int(y*weight)
    return(res1, res2)
def M(weight):
    x = 2.2
    y = 3.3
    res1 = int(x*weight)
    res2 = int(y*weight)
    return(res1, res2)
def L(weight):
    x = 1.1
    y = 1.54
    res1 = int(x*weight)
    res2 = int(y*weight)
    return(res1, res2)
def D_Z(weight):
    x = 1.76
    y = 2.2
    res1 = int(x*weight)
    res2 = int(y*weight)
    return(res1, res2)
def M_Z(weight):
    x = 2.2
    y = 2.64
    res1 = int(x*weight)
    res2 = int(y*weight)
    return(res1, res2)
def L_Z(weight):
    x = 1.1
    y = 1.54
    res1 = int(x*weight)
    res2 = int(y*weight)
    return(res1, res2)


def main():
    kor_x = 0.5    #koordinate x
    kor_y = 0.8      #koordinate y
    a=c.get()
    if a == 1:    #moški
        teza = c1.get()
        goal = c2.get()
        if goal == 0:
            messagebox.showerror(title='missed', message='blank field')
        elif goal == 1:
            m3 = Label(text=('You', 'should', 'eat', 'from', D(int(teza))[0], 'g', 'to', D(int(teza))[1], 'g', 'of', 'proteins'), font='1')
            m3.place(relx=kor_x, rely=kor_y, anchor='center')
        elif goal == 2:
            m3 = Label(text=('You', 'should', 'eat', 'from', M(int(teza))[0], 'g', 'to', M(int(teza))[1], 'g', 'of', 'proteins'), font='1')
            m3.place(relx=kor_x, rely=kor_y, anchor='center')
        elif goal == 3:
            m3 = Label(text=('You', 'should', 'eat', 'from', L(int(teza))[0], 'g', 'to', L(int(teza))[1], 'g', 'of', 'proteins'), font='1')
            m3.place(relx=kor_x, rely=kor_y, anchor='center')




        
    else:     #ženska
        teza = c1.get()
        goal = c2.get()
        if goal == 0:
            messagebox.showerror(title='missed', message='blank field')
        elif goal == 1:
            m3 = Label(text=('You', 'should', 'eat', 'from', D_Z(int(teza))[0], 'g', 'to', D_Z(int(teza))[1], 'g', 'of', 'proteins'), font='1')
            m3.place(relx=kor_x, rely=kor_y, anchor='center')
        elif goal == 2:
            m3 = Label(text=('You', 'should', 'eat', 'from', M_Z(int(teza))[0], 'g', 'to', M_Z(int(teza))[1], 'g', 'of', 'proteins'), font='1')
            m3.place(relx=kor_x, rely=kor_y, anchor='center')
        elif goal == 3:
            m3 = Label(text=('You', 'should', 'eat', 'from', L_Z(int(teza))[0], 'g', 'to', L_Z(int(teza))[1], 'g', 'of', 'proteins'), font='1')
            m3.place(relx=kor_x, rely=kor_y, anchor='center')






                





'''
while True:
    sex = input('Vnesi spol(M/Ž):')
    if not sex:
        break
    if sex == 'M' or 'm' or 'moški':
        weight = int(input('Enter your weight(in Kg):'))
        goal = input('Enter your goal(D-definition, M-gain mass, L-lose weight):')
        if goal == 'D':
            print('\n', 'You should eat from', D(weight)[0], 'g', 'to', D(weight)[1], 'g', 'of proteins', '\n')
            x = input('If you want to calculate again press enter, if you want to quit press enter double times')
        if goal == 'M':
            print('\n', 'You should eat from', M(weight)[0], 'g', 'to', M(weight)[1], 'g', 'of proteins', '\n')
            x = input('If you want to calculate again press enter, if you want to quit press enter double times')
        if goal == 'L':
            print('\n', 'You should eat from', L(weight)[0], 'g', 'to', L(weight)[1], 'g', 'of proteins', '\n')
            x = input('If you want to calculate again press enter, if you want to quit press enter double times')
    if sex == ('Ž' or 'ž' or 'ženska' or 'ženski'):
        weight = int(input('Enter your weight(in Kg):'))
        goal = input('Enter yoar goal(D-definition, M-gain mass, L-lose weight):')
        if goal == 'D':
            print('\n', 'You should eat from', D_Ž(weight)[0], 'g', 'to', D_Ž(weight)[1], 'g', 'of proteins', '\n')
            x = input('If you want to calculate again press enter, if you want to quit press enter double times')
        if goal == 'M':
            print('\n', 'You should eat from', M_Ž(weight)[0], 'g', 'to', M_Ž(weight)[1], 'g', 'of proteins', '\n')
            x = input('If you want to calculate again press enter, if you want to quit press enter double times')
        if goal == 'L':
            print('\n', 'You should eat from', L_Ž(weight)[0], 'g', 'to', L_Ž(weight)[1], 'g', 'of proteins', '\n')
            x = input('If you want to calculate again press enter, if you want to quit press enter double times')

'''





okno = Tk()

okno.geometry('450x450+20+20')      
okno.title('proteini')

'''
IZBERI SPOL
'''
m = Label(text='GENDER:', font='1')
m.place(relx=0.25, rely=0.07, anchor='center')

c=IntVar()

gumb_1 = Radiobutton(okno, text='men', value = 1, variable = c)
gumb_1.place(relx=0.7, rely=0.045, anchor='center')
gumb_2 = Radiobutton(okno, text='women', value = 2, variable = c)
gumb_2.place(relx=0.7, rely=0.105, anchor='center')


'''
IZBERI TEŽO
'''

m1 = Label(text='WEIGHT(in Kg):', font='1')
m1.place(relx=0.25, rely=0.225, anchor='center')

c1=StringVar()


vnos = Entry(okno, textvariable=c1)
vnos.place(relx=0.7, rely=0.225, anchor='center')


'''
IZBERI STYLE:
'''

m2 = Label(text='ENTER YOUR GOAL:', font='1')
m2.place(relx=0.25, rely=0.4, anchor='center')

c2=IntVar()

gumb_1 = Radiobutton(okno, text='Definition', value = 1, variable = c2)
gumb_1.place(relx=0.7, rely=0.34, anchor='center')
gumb_2 = Radiobutton(okno, text='Gain mass', value = 2, variable = c2)
gumb_2.place(relx=0.7, rely=0.4, anchor='center')
gumb_3 = Radiobutton(okno, text='fat burn, lose weight', value = 3, variable = c2)
gumb_3.place(relx=0.7, rely=0.46, anchor='center')


'''
CALCULATE
'''

gumb = Button(okno, text='CALCULATE', fg='blue', bg='green', command=main, font='1', height='2', width='20')
gumb.place(relx=0.5, rely=0.65, anchor='center')


'''
REZULTAT
'''





okno.mainloop()

