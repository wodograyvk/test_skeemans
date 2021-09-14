ask1 = int(input('сколько будет дважды два? '))
if ask1 == 4:
    print('правильный ответ')
else:
    print('это неверный ответ')
ask2 = int(input('сколько детей у Иакова? '))
if ask2 == 12:
    print('молодец!')
elif ask2 > 12:
    print('далеко')
elif ask2 < 12:
    print('недалеко от правды')
hum = str("кто я? человек?")
ask3 = str(input(hum))
if hum:
    print('таки, да')

