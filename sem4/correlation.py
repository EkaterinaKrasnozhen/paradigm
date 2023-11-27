# Простой коэффициент корреляции (Пирсона) вычисляется по формуле: r = n ∑ i = 1 (x n − ¯ x) (y n − ¯ y) n σ x σ y, 
# где n — число статистических наблюдений, x и y — случайные переменные. 

def correlation(data1: list[int], data2: list[int]) -> float:
    MEAN1 = sum(data1) / len(data1) # вычислим среднее значение data1
    MEAN2 = sum(data2) / len(data2) # вычислим среднее значение data2
    x_mean = list(map(lambda x: x - MEAN1, data1))# записываем разницу между каждым из отдельных значений data1 и его средним значением в список
    y_mean = list(map(lambda y: y - MEAN2, data2))# аналогично data2 
    sum_mult = sum([x * y for x, y in zip(x_mean, y_mean)]) # перемножаем значения из двух списков и находим сумму значений
    x_square = [x ** 2 for x in x_mean]# возводим в квадрат значения из списка
    y_square = [y ** 2 for y in y_mean]# аналогично возводим в квадрат второй список
    r = sum_mult / ((sum(x_square) * sum(y_square)) ** 0.5) # подставляем значения в формулу
    return r


x = [6, 12, 13, 17, 22, 25, 27, 29, 30, 32]
y = [45, 47, 39, 58, 68, 76, 75, 74, 78, 81]
result = correlation(x, y)
print(result)