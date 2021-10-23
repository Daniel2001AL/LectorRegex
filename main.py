import re_to_nfa
import my_nfa

REGEX = '(\w+\^\+|\(\w+\+*\w*\)\^\+)'



if __name__ == '__main__':
    #regex = input('Ingrese una expresión regular: ')
    regex = '(a+b)^++(a+b+epsilon)^*(b+c)^*'
    if '^+' in regex:
        regex = re_to_nfa.format_one_more(regex,REGEX)
    if 'epsilon' in regex:
        print('Es epsilon')
        regex = regex.replace('epsilon',"''")
    if '^*' in regex:
        print('Tiene ^*')
        regex = regex.replace('^*','*')

    new_nfa = re_to_nfa.re2nfa(regex)
    print(new_nfa)

    string = input('Ingrese una cadena: ')
    res = my_nfa.accepts_nfa(new_nfa,string)
    if res:
        print('Es válido')
    else:
        print('No es válido')