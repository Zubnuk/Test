# Занятие №1  
## Задачи  
1. В Файле main.py реализовать функцию *fibonacci*, принимающую порядковый номер числа фибоначчи   
и возвращающее соответствующее число фибоначи.  
2. В Файле main.py реализовать функцию *determinant*, принимающую квадратную целочисленную   
матрицу и возвращающую значение определителя данной матрицы.  
## Примечания  
- Функцию *fibonacci* необходимо реализовать в итерационном и рекурсивном вариантах.  
- Разработку вести в отдельных ветках, созданных на основе данной.  
- Корректность работы функции *fibonacci* можно проверить запустив файл test_fibonacci.py с модульными тестами.  
- Корректность работы функции *determinant* можно проверить запустив файл test_determinant.py с модульными тестами.  
- Правильность выполнения всего задания  можно проверить запустив файл test_runner.py, объединяющий все модульные тесты.  
  
## Числа фибоначчи  
**Числа Фибоначчи** — элементы числовой последовательности, в которой первые два числа равны 0 и 1,   
а каждое последующее число равно сумме двух предыдущих чисел. Названы в честь средневекового   
математика Леонардо Пизанского (известного как Фибоначчи).  
  
## Определитель матрицы  
**Матрицей** размера n×m, где n-число строк, m-число столбцов, называется таблица элементов, 
расположенных в определенном порядке. Элементы матрицы обозначаются a<sub>ij</sub>, где i – 
номер строки, а j – номер столбца. Если число столбцов матрицы равно числу строк (n=m), то матрица называется квадратной.  
<br/>**Определитель** – это числовая характеристика квадратной матрицы. Формулы разложения 
определителя по строке/столбцу позволяют сводить вычисление определителей к рекурсивной 
процедуре, использующей вычисление определителей меньших порядков.
<br/>Формула разложения определителя по i-ой строке 
$$det C=\sum_{j=1}^{n}c_{ij}A_{i}^{j}$$
где $A_{i}^{j}$ алгебраическое дополнение элемента c<sub>ij</sub>.
<br/>**Дополнительным  минором** произвольного элемента квадратной матрицы А называется 
определитель матрицы, полученной из исходной вычеркиванием i-ой строки и k-го столбца.
<br/>**Алгебраическим дополнением** элемента квадратной матрицы А называется его дополнительный 
минор, умноженный на (-1) в степени, равной сумме номеров строк и номеров столбцов, на
пересечении которых расположен элемент A<sub>ij</sub>.