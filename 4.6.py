a = 3
print('Глобальная переменная a = ', a)
y =9
print('Глобальная переменная y = ', y)
def func():
	print('Глобальная переменная a = ', a)
	y = 5
	print('Локальная переменная y = ', y)

func()
print('??? y = ', y)

x = 50
def func ():
        global x
        print('x равно', x)
        x = 2
        print('Заменяем глобальное значение х на ', x)
func()
print('Значение х составляет', x)
