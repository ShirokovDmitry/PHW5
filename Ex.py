# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

a = ('авб абввв баа абв ывваабв ыукк абв')
def Del_Word(s):
    return False if 'абв' in s else True
a = a.split()
print(a)
a = list(filter(Del_Word,a))
print(a)