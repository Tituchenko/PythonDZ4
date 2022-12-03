#B. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

import os.path


fileName1=''
while (os.path.exists (fileName1)==False):
    fileName1=input(f'Введите название файла №1:')
fileName2=''
while (os.path.exists (fileName2)==False):
    fileName2=input(f'Введите название файла №2:')
fileName3=input(f'Введите название итогового файла:')

f1 = open(fileName1, 'r')
equal1=f1.readline()
f1.close

f2 = open(fileName2, 'r')
equal2=f2.readline()
f2.close

def parserEqual (str):
    str=str.replace(' ','')
    str=str[:-2]
    str = str.replace('-', '+-')
    temp=str.split('+')
    ret={}
    for val in temp:
        if val!='':
            if val.isdigit():
                ret[0]=int(val)
            else:
                val2=val.replace('*','').split('x')

                if len(val2)==1:
                    val2.append('1')
                else:
                    if val2[1]=='':
                        val2[1]='1'
                ret[int(val2[1])] = int (val2[0])
    return ret

def summEqual(e1,e2):
    set1 = set(e1)
    set2 = set(e2)
    retSum={}
    maxI=0
    for i in set1.difference(set2):
        retSum[i]=e1[i]
        if i>maxI:
            maxI=i
    for i in set2.difference(set1):
        retSum[i]=e2[i]
        if i>maxI:
            maxI=i
    for i in set1.intersection(set2):
        retSum[i]=e1[i]+e2[i]
        if i>maxI:
            maxI=i
    for i in range(maxI):
        if not (i in retSum.keys()):
            retSum[i]=0
    return retSum


ret1=parserEqual (equal1)
ret2=parserEqual (equal2)
ret3=summEqual(ret1,ret2)

# не работает нормально import, зачем то базовый код запускает, а не просто функцию импортирует
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
    k=0
    for i in koef.keys():
       if i>k:
           k=i
    print (k)
    firstValue=k
    for i in range(k,-1,-1):
        equation+=addEqution(koef[i],i,i==firstValue)
        if koef[firstValue]==0: # Если последнего значения нет, то послдение переносим на единицу вперед
            firstValue+=-1
    equation+=' = 0'
    return equation




f3 = open(fileName3, 'a')
f3.write(createEqual(ret3))
f3.close

print (ret3)
