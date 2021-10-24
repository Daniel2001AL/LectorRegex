import re_to_nfa
import my_nfa

REGEX = '(\w+\^\+|\(\w+\+*\w*\)\^\+)'

def open_file(filename):
    with open(filename,'r',encoding='utf-8') as file:
        regex = file.read()
        regex = regex.replace('\n','')
        regex = regex.replace(' ','')
    return regex

def filter_regex(my_regex):
    if '^+' in my_regex:
        my_regex = re_to_nfa.format_one_more(my_regex,REGEX)
    if 'epsilon' in my_regex:
        print('Es epsilon')
        my_regex = my_regex.replace('epsilon',"''")
    if '^*' in my_regex:
        print('Tiene ^*')
        my_regex = my_regex.replace('^*','*')
    return my_regex

def run():
    regex = open_file('my_regex.txt')
    regex = filter_regex(regex)

    new_nfa = re_to_nfa.re2nfa(regex)
    print(new_nfa)

    string = input('Ingrese una cadena: ')
    res = my_nfa.accepts_nfa(new_nfa,string)
    if res:
        print('Es válido')
    else:
        print('No es válido')
if __name__ == '__main__':
    run()