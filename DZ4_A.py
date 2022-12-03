# A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
#
# НЕОБЯЗАТЕЛЬНОЕ, ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ:
# Расширить значение коэффициентов до [-100..100]

from random import randint
import os.path
k=int(input('Введите значение k:'))

defaultName='equal.txt'
fileName=input(f'Введите название файла (Enter - примется по-умолчанию {defaultName}):')
if fileName=='':
    fileName=defaultName

if (os.path.exists (fileName)):
    print ('Файл существует - будет добавлена формула в конец')
    equation = '\n'
else:
    equation = ''
    print('Файл не существует - будет создан')

koef={}
for i in range(k+1):
    koef[i]=randint(-100,100)

def addEqution (koeffi,powNum,firstValue):
    # Вначале разберемся со знаком в самом начале
    operator=''
    if (koeffi>0 and firstValue==False):
        operator=' + '
    elif (koeffi<0 and firstValue==False):
        operator = ' - '
        koeffi=-koeffi
    elif (koeffi < 0 and firstValue == True):
        operator = '-' # ну так же красивей без первого пробела
        koeffi=-koeffi
    # Теперь с кусоком со степенью в самом конце
    if powNum==0:
        powStr=''
    elif powNum==1:
        powStr = 'x'
    else:
        powStr = f'x**{powNum}'

    if powStr != '' and  koeffi!=1 and koeffi!=-1: # если коэффициенты не 1 или -1 то добавляем '*' вначало
        powStr=f'*{powStr}'

    if koeffi==0:
        return ''
    elif (koeffi==1 or koeffi==-1) and powStr!='': # Когда 1 или -1 и есть что напечатать после этого
        return f'{operator}{powStr}'
    else:
        return f'{operator}{koeffi}{powStr}'
def createEqual(koef,equation=''):
    firstValue=k
    for i in range(k,-1,-1):
        equation+=addEqution(koef[i],i,i==firstValue)
        if koef[firstValue]==0: # Если последнего значения нет, то послдение переносим на единицу вперед
            firstValue+=-1
    equation+=' = 0'
    return equation
equation=createEqual(koef,equation)
print (koef)
print (equation)

f1 = open(fileName, 'a')
f1.write(equation)
f1.close

