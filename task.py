array = input ("Введите массив чисел через запятую: ").split(",")
print (array)
d = int (input ("Значение дельты: "))
b = int (array [0])
c = 0
for i in range (len(array)):
    array[i] = int (array[i])
    if int (array[i]) < b:
        b = array[i]
for i in range (len(array)):
    if array[i] - b == d:
        c += 1
print (c)
