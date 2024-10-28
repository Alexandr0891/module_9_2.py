# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

'''В переменную first_result запишите список созданный при помощи сборки состоящий из длин строк списка first_strings,
 при условии, что длина строк не менее 5 символов.'''
first_result = [len(x) for x in first_strings if len(x) >= 5]
print(first_result)
'''В переменную second_result запишите список созданный при помощи сборки состоящий из пар слов(кортежей) одинаковой 
длины. Каждое слово из списка first_strings должно сравниваться с каждым из second_strings. (два цикла)'''
second_result = [ (x,y)  for x in first_strings  for y in second_strings if len(x) == len(y)  ]
print (second_result)
'''В переменную third_result запишите словарь созданный при помощи сборки, где парой ключ-значение будет строка-длина 
строки. Значения строк будут перебираться из объединённых вместе списков first_strings и second_strings.
 Условие записи пары в словарь - чётная длина строки.'''
third_result = [{x:len(x) for x in first_strings + second_strings if len(x) % 2 == 0}]
print (third_result)