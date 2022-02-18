import numpy as np 
import random

n = int(input('vvedite kolichestvo: '))
x =random.sample(range(1,n+10), n)# генерация размеров массивов
a = 1
for q in x:
	i = np.random.randint(10-n, n+10, q)# генерация массивов
	if a%2 == 0:
		print(sorted(i))
	else:
		print(sorted(i, reverse = True))
	a = a+1
