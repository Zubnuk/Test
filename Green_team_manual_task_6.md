### Green Team:    
  
$$      
A =       
 \begin{pmatrix}      
  -8 & 1 & 0 & \cdots & 0 & 0 \\      
  15 & -8 & 1 & \cdots & 0 & 0 \\      
  0 & 15 & -8 & \cdots & 0 & 0 \\      
  \vdots  & \vdots & \vdots & \ddots & \vdots & \vdots  \\      
  0 & 0 & 0 & \cdots & -8 & 1 \\      
  0 & 0 & 0 & \cdots & 15 & -8       
 \end{pmatrix}      
$$  
 
#### Задание: Найти определитель матрицы с порядком *n* = 8

$1.\bigtriangleup_n = -8 * \bigtriangleup_{n-1} - 15 * \bigtriangleup_{n-2}$
$\lambda^n = -8 * \lambda^{n-1} - 15 * \lambda^{n-2}$
$2.\lambda^n + 8 * \lambda^{n-1} + 15 * \lambda^{n-2} = 0$
$\lambda_1 = -5, \lambda_2 = -3$
$3.\bigtriangleup_n  = C_1 * \lambda_1^n + C_2 * \lambda_2^2$
$\text{Получаем систему:}$
$\left\{\begin{matrix}
-8 = -5 * C_1 -3 * C_2\\ 
49 = 25 * C_1 + 9 * C_2
\end{matrix}\right.$
$\text{Получаем значения: } C_1 = \frac52, C_2 = - \frac32$
$\text{Тогда: }$
$\bigtriangleup_n  = \frac52 * (-5)^n - \frac32 * (-3)^n$
$\text{Проверка: }$
$\bigtriangleup_1  = \frac52 * (-5)^1 - \frac32 * (-3)^1 = -8$
$\bigtriangleup_2  = \frac52 * (-5)^2 - \frac32 * (-3)^2 = 49$
$\text{Решение задачи: }$
$\bigtriangleup_8  = \frac52 * (-5)^8 - \frac32 * (-3)^8 = 966721$
$\text{Ответ: 966721.}$