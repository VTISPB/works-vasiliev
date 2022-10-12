print(5 > 3)
print(4 >= 4)
print(2 < 0)
print(-3 <= 3)
print(7 == 8)
print(6 != 1)

print(5 > 3)
print(4 >= 4)
print(2 < 0)
print(-3 <= 3)
print(7 == 8)
print(6 != 1)

x = int(input())

if x < 5:
	print(2 * x)
else:
	print(x + 9)

points = int(input('Баллы за семестр: '))

if points > 90:
    print('Отлично (A)')
elif points > 83:
    print('Хорошо (B)')
elif points > 74:
    print('Хорошо (C)')
elif points > 67:
    print('Удовлетворительно (D)')
elif points >= 60:
    print('Удовлетворительно (E)')
else:
    print('Неудовлетворительно (FX)')

x = float(input())
y = x ** 2 if x < 5 else 5 * x
print(y)