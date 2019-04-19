# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

a = [1,4,2,7,8,5,9,3,2,5,10,232,77,66,428,13]

def BubbleSort(array):
    for a in range(len(array)-1):
        for i in range(len(array)-1-a):
            if array[i]>array[i+1]:
                array[i],array[i+1] = array[i+1],array[i]
    return array

print(BubbleSort(a))
