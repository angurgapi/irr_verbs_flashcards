import pandas as pd
import random
import tkinter

 
window = tkinter.Tk()
window.title('Irregular verbs')

l1 = tkinter.Label (window, text="LET'S GO!", bg = 'orange', fg = 'blue', font = ("Helvetica", 33))
l1.pack()

l2 = tkinter.Label (window, text=" ", bg = 'orange', fg = 'blue', font = ("Helvetica", 33))
l2.pack()

l3 = tkinter.Label (window, text=" ", bg = 'orange', fg = 'blue', font = ("Helvetica", 33))
l3.pack()

window.configure(bg='orange')
window.geometry('600x250')

df =pd.read_csv('./irregular.csv')


def generate():
	guess = random.randint(0,376) 
	word = df.loc[guess][0]
	return word


def new_word():
	l1.configure(text=generate())
	l2.configure(text='')
	l3.configure(text='')


def full():
	inf = l1['text']
	idx = df.loc[df['infinitive']==inf].index[0]
	past_s = df.loc[idx][1]
	past_p = df.loc[idx][2]
	l2.configure(text=past_s)
	l3.configure(text=past_p)


nw_bt = tkinter.Button (window, text='NEW_VERB', bg="black", fg="white", command = new_word) 
nw_bt.pack()

rest_bt = tkinter.Button(window, text='CHECK YOURSELF', bg="black", fg="white", command = full)
rest_bt.pack()



window.mainloop()