"""
    Модуль threading используется для управления потоками 
    randint - генерирует случайное целое число 
"""
import threading
from random import randint  
import numpy as np

# i -строки, j-столбец    
def MultiMatrix(m1,m2,size):  

    """
        Обнуляем стобцы и строки матрицы 
    """           
    Matrix_Result = ([[randint(0, 0) for j in range(size)] for i in range(size)])  
    

    def Calculate(сm1, сm2, index, size):
        """
            Перемножение матриц
        """
        for j in range(size):
            sum_el=0
            for k in range(size):
                sum_el=sum_el+сm1[index][k]*сm2[j][k]
                Matrix_Result[index][j] = sum_el

         
    for i in range(size):
        """
            Создаем поток. Запускаем потоки. Каждая i-строка считается в новом потоке 
        """
        threading.Thread(target=Calculate, args=(m1, m2, i, size)).start()
        
    return Matrix_Result

print('------'*10)
    
print('\n')

print('Хардкод-квадратная матрица 3х3\n')

Matrix_Size = 3
Matrix_1 = np.array([(1, 2, 3), (32, 15, 6), (71, -8, 39)])
Matrix_2 = np.array([(-29, 32, 54), (-6, 25, 32), (22, -5, 10)])   

print('Матрица 1:\n', Matrix_1, '\n')
print('Матрица 2:\n', Matrix_2, '\n')

print('Умножение 1 на 2 с помощью потоков \n', np.array(MultiMatrix(Matrix_1,Matrix_2,Matrix_Size)))

print('\n')

print('------'*10)

print('\n')

print('Квадратная матрица с управляемой размерностью\n')

Matrix_Size = int(input('Введите размер матриц: '))

"""
    Формируем произвольную матрицу по j-столбцам и i-строкам по определнному вычислению
"""
Matrix_1 = np.array(([[randint(Matrix_Size*Matrix_Size*-1, Matrix_Size*Matrix_Size) for j in range(Matrix_Size)] for i in range(Matrix_Size)]))  
Matrix_2 = np.array(([[randint(Matrix_Size*Matrix_Size*-1, Matrix_Size*Matrix_Size) for j in range(Matrix_Size)] for i in range(Matrix_Size)]))  

print('Матрица 1:\n', Matrix_1, '\n')
print('Матрица 2:\n', Matrix_2, '\n')

print('Умножение 1 на 2 с помощью потоков \n', np.array(MultiMatrix(Matrix_1,Matrix_2,Matrix_Size)))
