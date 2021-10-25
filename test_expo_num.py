import re

string_1 = 'a^3'
string_2 = '(a+b)^23'
string_3 = '(c+d)^2'

expected_string_1 = '(a)(a)(a)'
expected_string_3 = '(c+d)(c+d)'

REGEX = '(\w+\^[0-9]+|\(\w+\+*\w*\)\^[0-9]+)'

def format_expo_num(string):
    search_num = re.compile(REGEX)
    expression = search_num.search(string).group(1)
    number = re.search('[0-9]+',expression).group(0)
    new_e = re.sub('\^[0-9]+','',expression)
    if '(' not in new_e and ')' not in new_e:
            new_e = '('+new_e+')'
    new_string = new_e * int(number)
    return new_string

if __name__ == '__main__':
    a = format_expo_num(string_1)
    print(a)
    res =re.match(r'.*\^[0-9]+','a^2')
    if res:
        print('Match')