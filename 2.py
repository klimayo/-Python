time = int(input('ввод числа:'))
h = time /3600
m = time % 3600/ 60
s = time % 3600 % 60

print('%i:%i:%i' % (h, m, s))