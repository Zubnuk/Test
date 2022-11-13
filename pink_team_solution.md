## Дана матрица, нужно найти определитель n=9 порядка

$$      
A =       
 \begin{pmatrix}      
  4 & 3 & 0 & \cdots & 0 & 0 \\      
  -4 & 4 & 3 & \cdots & 0 & 0 \\      
  0 & -4 & 4 & \cdots & 0 & 0 \\      
  \vdots  & \vdots & \vdots & \ddots & \vdots & \vdots  \\      
  0 & 0 & 0 & \cdots & 4 & 3 \\      
  0 & 0 & 0 & \cdots & -4 & 4       
 \end{pmatrix}      
$$ 

$1) \bigtriangleup_n = 4 * \bigtriangleup_{n-1} - 12 * \bigtriangleup_{n-2}$

$2) \lambda^n - 4 * \lambda^{n-1} + 12 * \lambda^{n-2} = 0| :\lambda^{n-2}$

$λ ^2 - 4λ + 12 = 0$

$D = 64$

$\lambda_1 = 6, \lambda_2 = -2$

$3)\bigtriangleup_n  = C_1 * \lambda_1^n + C_2 * \lambda_2^n$

$\text{Система:}$  

$(4 = C_1 * 6 + C_2 * (-2);$  

$28 = C_1 * 36 + C_2 * 4)$

$\text C_1 = \frac34, C_2 = \frac14$

$\text{Тогда: }$

$\bigtriangleup_n  = \frac34 * 6^n + \frac14 * (-2 )^n$

$\bigtriangleup_{9}  = \frac34 *  6^{9} - \frac14 * 2^{9}=7558144$

$\text{Ответ: 7558144}$
