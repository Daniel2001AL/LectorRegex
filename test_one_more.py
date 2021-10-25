import re
from tkinter.constants import NONE


strings = ['(a+b)^+','ab^+','(a+b)^++(a+b+epsilon)^*(b+c)^*']

expected_string = ['(a+b)(a+b)*','(ab)(ab)*','(a+b)(a+b)*+(a+b+epsilon)^*(b+c)^*']

REGEX = '(\w+\^\+|\(\w+\+*\w*\)\^\+)'

def first_try():
    index = strings[0].index('^+')
    simbolos = ['^+','*','(',')']
    new_s = ''
    for i in reversed(strings[0]):
        if i not in simbolos:
            new_s = new_s+i
    my_s = ''
    for i in reversed(new_s):
        my_s = my_s+i
    print(my_s)
    my_s = my_s.replace('^+','')
    my_s = '('+my_s+')'+'('+my_s+')'+'*'
    print(my_s)
    print('Original: ',strings[0])


def second_try():
    expo_one_more =[]
    for string in strings:
        find = re.search(REGEX,string)
        expression = find.group(1)
        expo_one_more.append(expression)
        print(expression)
    for i,e in enumerate(expo_one_more):
        new_e = e.replace('^+','')
        print(new_e)
        if '(' not in new_e and ')' not in new_e:
            new_e = '('+new_e+')'
        expo_one_more[i] = (e,new_e)
    print(expo_one_more)

    for i in range(len(strings)):
        new_expression = strings[i]
        new_expression = new_expression.replace(expo_one_more[i][0],
                                    f'{expo_one_more[i][1]}{expo_one_more[i][1]}*')
        print(new_expression)
        if new_expression == expected_string[i]:
            print('Ya quedó')


def format_one_more(my_expression):
    print(my_expression)
    find = re.search(REGEX,my_expression)
    if find is not None:
        expression = find.group(1)
        print(expression)
        new_e = expression.replace('^+','')
        if '(' not in new_e and ')' not in new_e:
                new_e = '('+new_e+')'
        my_expression = my_expression.replace(expression,f'{new_e}{new_e}*')
        print('Original: ', my_expression)
        print('Formateado: ',my_expression)
    return (my_expression,find)
if __name__ == '__main__':
    #my_regex = '(a+b)^++(a+b+epsilon)^*(b+c)^*'
    my_regex = '(a+b)^+(x+epsilon)^+'
    #my_regex = '(a+b)(a+b)*'
    find_patterns = ''
    while find_patterns is not None:
        res = format_one_more(my_regex)
        my_regex = res[0]
        find_patterns = res[1]
        

    print(my_regex)
    if '^*' in my_regex:
        print('Tiene ^*')
        my_regex = my_regex.replace('^*','*')
    if 'epsilon' in my_regex:
        print('Es epsilon')
        my_regex = my_regex.replace('epsilon',"''")
    print(my_regex)
    pattern = re.compile(REGEX)
    for matches in re.findall(pattern,my_regex):
        print('a')

    