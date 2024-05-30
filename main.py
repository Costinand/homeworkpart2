from fake_math import divide as f_d
from true_math import divide as t_d

num_ar = [57, 6], [14, 0]
for i in num_ar:
    first = i[0]
    second = i[1]
    f_d(first, second)
    t_d(first, second)

