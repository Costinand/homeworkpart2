
import random
number = random.randint(3, 20)
print('n: ', number)

basket_w = [] # назвал "чудесная корзина", она станет тем, что попросили назвать result, но потом оставил рабочее назваение
t = int((number - 1 )/ 2)
y = t + 1
for p in range(1 , y):
    d = number - p
    basket_w.append(d)
    basket_w.append(p)
sim_num = [2, 3, 4, 5, 6, 7, 9]
for s in sim_num:
    k = number / s
    k1 = int(k)
    if k == k1:
        # предполагаю, что можно как-то использовать блок кода с 7 по 12, но пока не смог найти способа. поэтому дублирую
        t = int((k1 - 1) / 2)
        y = t + 1
        for p in range(1, y):
            d = k1 - p
            basket_w.append(d)
            basket_w.append(p)
print('result: ', basket_w)












