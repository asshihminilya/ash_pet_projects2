# put your python code here
var = input()
try:
    num = int(var)
    if not 0 < num <= 3:
        raise ValueError('Число вне диапазона')
    print(var)

except:
    print('Некорректный ввод')


