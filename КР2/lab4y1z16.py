#В каждой строке матрицы максимальный элеменет переместить в конец строки не меняя поряок отсальных элементов

import numpy as np

a = np.array([[8, 4, 3,6],
              [3, 2, 5,1],
              [4, 32, 6,2]])
result = []
for i in a:
    max_in = np.argmax(i)
    max_el = i[max_in]
    i = np.delete(i, max_in)
    i = np.append(i, max_el)
    result.append(i)
print(np.array(result))