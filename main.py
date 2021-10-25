#!/usr/bin/python
from tkinter import Button, Entry, Label, Tk
from tkinter import font, messagebox

from regex_engine import re2nfa
from regex_engine.re_to_nfa import format_expo_num, format_one_more
from regex_engine import accepts_nfa
import re

REGEX_ONE_MORE = '(\w+\^\+|\(\w+\+*\w*\)\^\+)'

REGEX_EXPO_NUMBER = '(\w+\^[0-9]+|\(\w+\+*\w*\)\^[0-9]+)'

def filter_regex(my_regex):
    if '^+' in my_regex:
        my_regex = my_regex.replace('^++','^+')
        my_regex = format_one_more(my_regex,REGEX_ONE_MORE)
    if re.match(r'.*\^[0-9]+',my_regex):
        my_regex = format_expo_num(my_regex,REGEX_EXPO_NUMBER)
        my_regex = my_regex.replace(')+',')')
        my_regex = my_regex.replace('+(','(')
    if 'epsilon' in my_regex:
        my_regex = my_regex.replace('epsilon',"''")
    if '^*' in my_regex:
        my_regex = my_regex.replace('^*+','^*')
        my_regex = my_regex.replace('^*','*')
    return my_regex

def run():
    string = ''
    regex = regex_field.get()
    if regex != '':
        my_label['text'] ='Expresión Regular: '
        regex_label['text'] = regex
        regex = filter_regex(regex)
        new_nfa = re2nfa(regex)
        string = text_field.get()
        res = accepts_nfa(new_nfa,string)
        if res:
            messagebox.showinfo(message='Es válido',title='Resultado')
        else:
            messagebox.showerror(message='NO es válido',title='Resultado')
    else:   messagebox.showerror(message='Ingrese una expresión regular',title='Error')


    

if __name__ == '__main__':
    root = Tk()
    root.title('Lector de REGEX')
    root.geometry('1280x720')

    label_title_regex = Label(root,text='Ingrese la Expresión Regular', 
                        width=25,height=1)
    label_title_regex.place(x=470,y=50)
    label_title_regex['font'] = font.Font(size=12)

    regex_field = Entry(root, width=20)
    regex_field['font'] = font.Font(size=12)
    regex_field.place(x=500,y=100)


    label_title_regex = Label(root,text='Ingrese la cadena a evaluar', 
                        width=25,height=1)
    label_title_regex.place(x=470,y=200)
    label_title_regex['font'] = font.Font(size=12)

    text_field = Entry(root, width=20)
    text_field['font'] = font.Font(size=12)
    text_field.place(x=500,y=250)

    regex_label = Label(root,width=40)
    regex_label['font'] = font.Font(size=12)
    regex_label.place(x=50,y=400)
    my_label = Label(root,width=19)
    my_label['font'] = font.Font(size=12)
    my_label.place(x=50,y=370)

    btn_process_regex = Button(root,text='Procesar cadena', command=run)
    btn_process_regex.place(x=530,y=330)
    btn_process_regex['font'] = font.Font(size=13)

    root.mainloop()