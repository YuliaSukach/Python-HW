# Создать 3 переменные с одинаковыми данными и с одинаковыми идентификаторами

a = 3
b = a
c = b

assert id(a) == id(b) == id(c)