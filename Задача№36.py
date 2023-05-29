# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. 
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). Примечание: 
# бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

def print_operation_table(operation, num_rows, num_сolumns):
    for i in range(1, num_rows + 1):
        answer = []
        for j in range(1, num_сolumns + 1):
            answer.append(str(operation(i, j)))
        print(''.join(f'{e:<4}' for e in answer))


line = int(input("Введите количество строк: "))
columns = int(input("Введите количество столбцов: "))

print_operation_table(lambda x, y: x * y, line, columns)