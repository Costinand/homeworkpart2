
import random
number = random.randint(3, 20)
#print('n: ', number)

basket_w = [] # назвал "чудесная корзина", она станет тем, что попросили назвать result, но потом оставил рабочее назваение
t = int((number - 1 )/ 2)
y = t + 1
for p in range(1 , y):
    d = number - p
    small_bskt = p, d #формирование кортежа для списка кортежей
   # print(small_bskt)
    basket_w.append(small_bskt)
  #  basket_w.append(p)
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
            small_bskt = p, d
            #basket_w.append(d)
            basket_w.append(small_bskt) #формирование кортежа для списка кортежей
            basket_w.sort()
#print('result: ', basket_w)   #список из списка кортежей
result =list(sum(basket_w, ()))
#print(result)
result_ = ''.join(str(item) for item in result)
print(number, ' - ' , result_)